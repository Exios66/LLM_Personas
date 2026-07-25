#!/usr/bin/env python3
"""Render and publish the MORNINGSTAR Quarto site to JackJBurleson Posit Connect Cloud.

Creates a **new** content item on first run (does not touch the PSYCH 755 manuscript
content id 019f9a10-ebb9-d1d5-839f-97e794bfd0ca). Subsequent runs update the id
stored in `_publish.yml`.

Auth:
  - env POSIT_CONNECT_CLOUD_ACCESS_TOKEN (+ REFRESH_TOKEN, ACCOUNT_ID), or
  - /tmp/posit-tokens.json from a prior device flow, or
  - interactive device-code flow
"""

from __future__ import annotations

import argparse
import io
import json
import os
import re
import shutil
import subprocess
import sys
import tarfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POSIT = ROOT / "posit"
ACCOUNT_NAME = "jackjburleson"
TITLE = "MORNINGSTAR — LLM Personas Courtroom"
API = "https://api.connect.posit.cloud/v1"
AUTH_HOST = "login.posit.cloud"
CLIENT_ID = "quarto-cli"
SCOPE = "vivid"
PUBLISH_YML = POSIT / "_publish.yml"
# Never overwrite the PSYCH 755 manuscript content.
FORBIDDEN_CONTENT_IDS = {"019f9a10-ebb9-d1d5-839f-97e794bfd0ca"}


def _log(msg: str) -> None:
    print(msg, flush=True)


def run(cmd: list[str], *, cwd: Path = ROOT) -> None:
    _log("$ " + " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


def ensure_quarto() -> None:
    if shutil.which("quarto") is None:
        raise SystemExit("quarto not on PATH; install Quarto ≥ 1.10")
    out = subprocess.check_output(["quarto", "--version"], text=True).strip()
    _log(f"quarto {out}")


def build_pages() -> None:
    run([sys.executable, str(ROOT / "scripts" / "build_posit_site_pages.py")])


def render_site() -> Path:
    ensure_quarto()
    build_pages()
    run(["quarto", "render"], cwd=POSIT)
    site = POSIT / "_site"
    if not (site / "index.html").is_file():
        raise SystemExit("quarto render did not produce posit/_site/index.html")
    return site


def post_form(url: str, data: dict[str, str]) -> dict:
    body = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"},
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())


def device_auth() -> dict:
    auth = post_form(
        f"https://{AUTH_HOST}/oauth/device/authorize",
        {"scope": SCOPE, "client_id": CLIENT_ID},
    )
    _log("=" * 72)
    _log("AUTHORIZE NOW (Posit Connect Cloud / JackJBurleson)")
    _log("=" * 72)
    _log(f"URL:  {auth['verification_uri_complete']}")
    _log(f"CODE: {auth['user_code']}")
    _log("=" * 72)
    Path("/tmp/posit-device-auth.json").write_text(json.dumps(auth, indent=2), encoding="utf-8")
    interval = max(int(auth.get("interval", 5)), 5)
    expires = int(auth.get("expires_in", 1800))
    start = time.time()
    while True:
        if time.time() - start > expires:
            raise SystemExit("Device authorization timed out.")
        try:
            tok = post_form(
                f"https://{AUTH_HOST}/oauth/token",
                {
                    "scope": SCOPE,
                    "client_id": CLIENT_ID,
                    "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
                    "device_code": auth["device_code"],
                },
            )
            _log(f"Authorized after {time.time() - start:.0f}s")
            Path("/tmp/posit-tokens.json").write_text(json.dumps(tok, indent=2), encoding="utf-8")
            return tok
        except urllib.error.HTTPError as e:
            raw = e.read().decode()
            try:
                code = json.loads(raw).get("error", raw)
            except Exception:
                code = raw.strip()
            if code == "authorization_pending":
                time.sleep(interval)
                continue
            if code == "slow_down":
                interval += 5
                time.sleep(interval)
                continue
            raise SystemExit(f"OAuth error: {code}")


def load_tokens() -> tuple[str, str | None]:
    access = os.environ.get("POSIT_CONNECT_CLOUD_ACCESS_TOKEN")
    refresh = os.environ.get("POSIT_CONNECT_CLOUD_REFRESH_TOKEN")
    if access:
        _log("Using POSIT_CONNECT_CLOUD_* environment tokens")
        return access, refresh
    cached = Path("/tmp/posit-tokens.json")
    if cached.is_file():
        tok = json.loads(cached.read_text(encoding="utf-8"))
        if tok.get("access_token"):
            _log("Using /tmp/posit-tokens.json")
            return tok["access_token"], tok.get("refresh_token")
    tok = device_auth()
    return tok["access_token"], tok.get("refresh_token")


def api(
    method: str,
    path: str,
    access: str,
    body: dict | None = None,
) -> dict | None:
    data = None if body is None else json.dumps(body).encode()
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {access}",
        "User-Agent": "llm-personas-posit-publish/1.0",
    }
    if body is not None:
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(f"{API}/{path}", data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req) as r:
            raw = r.read()
            return json.loads(raw.decode()) if raw else None
    except urllib.error.HTTPError as e:
        raise SystemExit(f"{method} {path} → {e.code}: {e.read().decode()[:800]}") from e


def assert_writable_account(access: str) -> str:
    accounts = api("GET", "accounts?has_user_role=true", access) or {}
    rows = accounts.get("data") or []
    names = [a.get("name") for a in rows]
    _log(f"Authorized accounts: {names}")
    for a in rows:
        if a.get("name") == ACCOUNT_NAME:
            return a["id"]
    env_id = os.environ.get("POSIT_CONNECT_CLOUD_ACCOUNT_ID")
    if env_id:
        return env_id
    if not rows:
        raise SystemExit("No publishable Posit accounts for this login.")
    _log(f"WARNING: '{ACCOUNT_NAME}' not in account list; using {rows[0].get('name')}")
    return rows[0]["id"]


def read_publish_yml_id() -> str | None:
    if not PUBLISH_YML.is_file():
        return None
    text = PUBLISH_YML.read_text(encoding="utf-8")
    m = re.search(r"id:\s*([0-9a-fA-F-]{36})", text)
    if not m:
        return None
    cid = m.group(1)
    if cid in FORBIDDEN_CONTENT_IDS:
        raise SystemExit(
            f"_publish.yml points at forbidden PSYCH 755 content id {cid}. Refusing."
        )
    return cid


def write_publish_yml(content_id: str) -> None:
    ui = f"https://connect.posit.cloud/{ACCOUNT_NAME}/content/{content_id}"
    PUBLISH_YML.write_text(
        "- source: project\n"
        "  posit-connect-cloud:\n"
        f"    - id: {content_id}\n"
        f"      url: {ui}\n",
        encoding="utf-8",
    )
    _log(f"Wrote {PUBLISH_YML}")


def make_bundle(site: Path) -> bytes:
    buf = io.BytesIO()
    files = sorted(p for p in site.rglob("*") if p.is_file())
    manifest = {
        "version": 1,
        "locale": "en_US",
        "platform": "4.0.0",
        "metadata": {"appmode": "static", "primary_rmd": None, "primary_html": "index.html"},
        "packages": None,
        "files": {p.relative_to(site).as_posix(): {"checksum": ""} for p in files},
        "users": None,
    }
    with tarfile.open(fileobj=buf, mode="w:gz") as tar:
        man = json.dumps(manifest).encode()
        info = tarfile.TarInfo("manifest.json")
        info.size = len(man)
        tar.addfile(info, io.BytesIO(man))
        for p in files:
            tar.add(p, arcname=p.relative_to(site).as_posix())
    return buf.getvalue()


def create_content(access: str, account_id: str) -> dict:
    _log(f"Creating new Connect Cloud content: {TITLE!r}")
    created = api(
        "POST",
        "contents",
        access,
        {
            "account_id": account_id,
            "title": TITLE,
            "next_revision": {
                "source_type": "bundle",
                "content_type": "static",
                "app_mode": "static",
                "primary_file": "index.html",
            },
            "secrets": [],
        },
    )
    if not created or not created.get("id"):
        raise SystemExit(f"create content failed: {created}")
    cid = created["id"]
    if cid in FORBIDDEN_CONTENT_IDS:
        raise SystemExit("API returned forbidden content id; aborting.")
    write_publish_yml(cid)
    return created


def publish_bundle(access: str, site: Path, content_id: str) -> dict:
    if content_id in FORBIDDEN_CONTENT_IDS:
        raise SystemExit("Refusing to publish to PSYCH 755 content id.")

    updated = api(
        "PATCH",
        f"contents/{content_id}?new_bundle=true",
        access,
        {
            "secrets": [],
            "revision_overrides": {"primary_file": "index.html", "app_mode": "static"},
        },
    ) or {}
    rev = updated.get("next_revision") or updated.get("current_revision") or {}
    upload_url = rev.get("source_bundle_upload_url")
    if not upload_url:
        # Fresh create may already expose upload URL on the create response revision
        content = api("GET", f"contents/{content_id}", access) or {}
        rev = content.get("next_revision") or content.get("current_revision") or {}
        upload_url = rev.get("source_bundle_upload_url")
    if not upload_url:
        raise SystemExit(f"No upload URL for content {content_id}: {updated}")

    bundle = make_bundle(site)
    _log(f"Uploading bundle ({len(bundle)} bytes)")
    req = urllib.request.Request(
        upload_url,
        data=bundle,
        method="POST",
        headers={"Content-Type": "application/gzip"},
    )
    with urllib.request.urlopen(req) as r:
        _log(f"upload_status {r.status}")

    req = urllib.request.Request(
        f"{API}/contents/{content_id}/publish",
        method="POST",
        headers={
            "Accept": "application/json",
            "Authorization": f"Bearer {access}",
            "User-Agent": "llm-personas-posit-publish/1.0",
        },
    )
    with urllib.request.urlopen(req) as r:
        _log(f"publish_http {r.status}")
        r.read()

    share_fallback = f"https://{content_id}.share.connect.posit.cloud/"
    ui_url = f"https://connect.posit.cloud/{ACCOUNT_NAME}/content/{content_id}"
    for i in range(60):
        content = api("GET", f"contents/{content_id}", access) or {}
        rev = content.get("current_revision") or {}
        result = rev.get("publish_result")
        status = rev.get("status") or rev.get("state")
        url = rev.get("url")
        _log(f"poll[{i}] status={status} result={result} url={url}")
        if result == "success" or status == "published":
            return {
                "content": content,
                "share_url": url or share_fallback,
                "ui_url": ui_url,
                "content_id": content_id,
            }
        if result and result not in {"success", "running", None}:
            raise SystemExit(
                f"Publish failed: {rev.get('publish_error_code')} {rev.get('publish_error_args')}"
            )
        time.sleep(3)
    raise SystemExit("Timed out waiting for publish success")


def verify_live(share_url: str, *, expect_substrings: list[str]) -> None:
    req = urllib.request.Request(share_url, headers={"User-Agent": "llm-personas-posit-publish/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        html = r.read().decode("utf-8", "replace")
        code = r.status
    if code != 200:
        raise SystemExit(f"Live verify HTTP {code}")
    missing = [s for s in expect_substrings if s not in html]
    if missing:
        raise SystemExit(f"Live page missing expected strings: {missing}")
    _log(f"Live verification OK ({len(html)} bytes): {share_url}")
    try:
        from playwright.sync_api import sync_playwright

        art = Path("/opt/cursor/artifacts")
        art.mkdir(parents=True, exist_ok=True)
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(share_url, wait_until="networkidle", timeout=90000)
            page.screenshot(path=str(art / "morningstar-connect-cloud.png"), full_page=False)
            browser.close()
        _log(f"Screenshot → {art / 'morningstar-connect-cloud.png'}")
    except Exception as exc:  # noqa: BLE001
        _log(f"Screenshot skipped: {exc}")


def patch_quarto_site_url(content_id: str) -> None:
    yml = POSIT / "_quarto.yml"
    text = yml.read_text(encoding="utf-8")
    site_url = f"https://connect.posit.cloud/{ACCOUNT_NAME}/content/{content_id}"
    if "site-url:" in text:
        text = re.sub(r"site-url:\s*.*", f"site-url: {site_url}", text, count=1)
    else:
        text = text.replace(
            '  title: "MORNINGSTAR"\n',
            f'  title: "MORNINGSTAR"\n  site-url: {site_url}\n',
            1,
        )
    yml.write_text(text, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--skip-render", action="store_true", help="Publish existing _site/")
    p.add_argument(
        "--content-id",
        default=None,
        help="Existing MORNINGSTAR content id (default: read _publish.yml or create new)",
    )
    p.add_argument(
        "--expect",
        action="append",
        default=[],
        help="Substring that must appear on the live share page (repeatable)",
    )
    args = p.parse_args(argv)

    if not args.skip_render:
        site = render_site()
    else:
        site = POSIT / "_site"
        if not (site / "index.html").is_file():
            raise SystemExit("posit/_site/index.html missing; refuse --skip-render")

    access, _refresh = load_tokens()
    account_id = assert_writable_account(access)
    _log(f"Using account_id={account_id}")

    content_id = args.content_id or read_publish_yml_id()
    if content_id:
        if content_id in FORBIDDEN_CONTENT_IDS:
            raise SystemExit("Refusing forbidden PSYCH 755 content id.")
        _log(f"Updating existing content {content_id}")
    else:
        created = create_content(access, account_id)
        content_id = created["id"]
        # Prefer upload URL from create response when present
        rev = created.get("next_revision") or {}
        if rev.get("source_bundle_upload_url"):
            _log("Create response includes upload URL; proceeding to publish_bundle")

    result = publish_bundle(access, site, content_id)
    write_publish_yml(content_id)
    patch_quarto_site_url(content_id)

    expect = list(args.expect) or ["MORNINGSTAR", "Operational Agent Swarm", "Lucius"]
    verify_live(result["share_url"], expect_substrings=expect)

    out = {
        **result,
        "account": ACCOUNT_NAME,
        "title": TITLE,
    }
    Path("/tmp/posit-morningstar-publish-result.json").write_text(
        json.dumps(out, indent=2, default=str), encoding="utf-8"
    )
    _log("UI_URL " + result["ui_url"])
    _log("SHARE_URL " + result["share_url"])
    _log("CONTENT_ID " + content_id)
    _log("DONE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
