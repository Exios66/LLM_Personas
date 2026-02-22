"""
Cryptographic proof for executive overrides of judicial decisions.

When the executive must override a judicial decision (emergency, explicit court approval),
it must attach a proof: HMAC-SHA256(secret, payload) where payload = ruling_id || reason || timestamp.
"""

import hashlib
from typing import Optional
import hmac
import os
import secrets
from pathlib import Path


SEPARATOR = "||"
SECRET_ENV = "EXECUTIVE_PROOF_SECRET"
DEFAULT_SECRET_PATH = Path(__file__).resolve().parent / ".executive_secret"


def _get_secret(secret_path=None):
    """Load secret from env or file. Raises if not found."""
    if os.environ.get(SECRET_ENV):
        raw = os.environ[SECRET_ENV].strip()
        if raw.startswith("0x"):
            raw = raw[2:]
        return bytes.fromhex(raw)
    path = Path(secret_path) if secret_path else DEFAULT_SECRET_PATH
    if path.exists():
        with open(path, "rb") as f:
            return f.read().strip()
    raise FileNotFoundError(
        f"Executive proof secret not found. Set {SECRET_ENV} or create {path}."
    )


def _payload(ruling_id: str, override_reason: str, timestamp: str) -> bytes:
    """Canonical payload for HMAC."""
    return f"{ruling_id}{SEPARATOR}{override_reason}{SEPARATOR}{timestamp}".encode(
        "utf-8"
    )


class OverrideProof:
    """
    Generate and verify cryptographic proof for executive overrides.

    Proof = HMAC-SHA256(secret, ruling_id || override_reason || timestamp).
    """

    @staticmethod
    def generate(
        ruling_id: str,
        override_reason: str,
        timestamp: Optional[str] = None,
        secret_path=None,
    ) -> str:
        """
        Generate proof for an override.

        Args:
            ruling_id: Court ruling ID being overridden
            override_reason: Reason for override (e.g., emergency, court approval)
            timestamp: ISO 8601 (default: now UTC)
            secret_path: Path to secret file (default: executive/.executive_secret)

        Returns:
            Hex-encoded HMAC-SHA256 proof.
        """
        from datetime import datetime, timezone

        if timestamp is None:
            timestamp = datetime.now(timezone.utc).isoformat()

        secret = _get_secret(secret_path)
        payload = _payload(ruling_id, override_reason, timestamp)
        signature = hmac.new(secret, payload, hashlib.sha256).hexdigest()
        return f"{timestamp}{SEPARATOR}{signature}"

    @staticmethod
    def verify(
        proof: str,
        ruling_id: str,
        override_reason: str,
        secret_path=None,
    ) -> Optional[str]:
        """
        Verify proof. Returns timestamp if valid, None if invalid.

        Args:
            proof: Output of generate() (timestamp||signature)
            ruling_id: Court ruling ID
            override_reason: Reason for override
            secret_path: Path to secret file

        Returns:
            Timestamp string if valid, None if invalid.
        """
        parts = proof.split(SEPARATOR, 1)
        if len(parts) != 2:
            return None
        timestamp, signature = parts

        secret = _get_secret(secret_path)
        payload = _payload(ruling_id, override_reason, timestamp)
        expected = hmac.new(secret, payload, hashlib.sha256).hexdigest()
        if hmac.compare_digest(expected, signature):
            return timestamp
        return None

    @staticmethod
    def generate_secret_file(path=None) -> str:
        """
        Generate a new secret and write to file. Returns hex-encoded secret.

        Use for initial setup: create executive/.executive_secret
        """
        path = Path(path) if path else DEFAULT_SECRET_PATH
        secret = secrets.token_hex(32)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            f.write(secret)
        return secret
