"""Fictional customer portal demo: no persistent accounts or real credentials."""
import secrets
import time

def register_customer(name: str, email: str) -> dict:
    name = name.strip()
    email = email.strip().lower()
    local, separator, domain = email.partition("@")
    if (not name or not separator or not local or not domain
            or "@" in domain or any(char.isspace() for char in email)
            or "." not in domain or any(not part for part in domain.split("."))):
        raise ValueError("Name and a valid email are required")
    return {"name": name, "email": email, "status": "registered"}


def update_profile(profile: dict, name: str) -> dict:
    name = name.strip()
    if not name:
        raise ValueError("Name is required")
    return {**profile, "name": name}


def recovery_confirmation(email: str) -> dict:
    # Demo only: no account lookup, email sending, or credential reset.
    return {"message": "If an account exists, recovery instructions will be sent."}


def dashboard_preferences(theme: str, page_size: int) -> dict:
    if theme not in {"light", "dark"} or page_size not in {10, 25, 50}:
        raise ValueError("Unsupported dashboard preference")
    return {"theme": theme, "page_size": page_size}


def dashboard_state(records: list) -> dict:
    return {"empty": not records, "count": len(records),
            "message": "No records yet" if not records else "Records available"}


class DemoSessions:
    """In-memory sessions for a pre-authenticated fictional demo user."""

    def __init__(self, lifetime_seconds: int = 900):
        if lifetime_seconds <= 0:
            raise ValueError("Session lifetime must be positive")
        self._lifetime = lifetime_seconds
        self._sessions = {}

    def start(self, verified_demo_identity: str) -> str:
        if not verified_demo_identity.strip():
            raise ValueError("Verified demo identity is required")
        token = secrets.token_urlsafe(32)
        self._sessions[token] = (verified_demo_identity, time.monotonic() + self._lifetime)
        return token

    def identity(self, token: str):
        session = self._sessions.get(token)
        if session is None:
            return None
        identity, expires = session
        if time.monotonic() >= expires:
            self.end(token)
            return None
        return identity

    def end(self, token: str) -> None:
        self._sessions.pop(token, None)
