"""Gmail delivery for Research Report workflow.

Supports SMTP (GMAIL_USER + GMAIL_APP_PASSWORD) or Gmail API (when configured).
"""

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Optional


def send_report_email(
    html_body: str,
    subject: str,
    to_email: str,
    *,
    from_email: Optional[str] = None,
) -> None:
    """
    Send an HTML email via Gmail SMTP.

    Requires GMAIL_USER and GMAIL_APP_PASSWORD environment variables.
    Use an App Password (not regular password) for Gmail accounts with 2FA.
    """
    user = (from_email or os.environ.get("GMAIL_USER", "")).strip()
    password = os.environ.get("GMAIL_APP_PASSWORD", "").strip()

    if not user or not password:
        raise ValueError(
            "Gmail credentials required. Set GMAIL_USER and GMAIL_APP_PASSWORD. "
            "Use App Password for accounts with 2FA: "
            "https://support.google.com/accounts/answer/185833"
        )

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = user
    msg["To"] = to_email
    msg.attach(MIMEText(html_body, "html", "utf-8"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(user, password)
        server.sendmail(user, to_email, msg.as_string())
