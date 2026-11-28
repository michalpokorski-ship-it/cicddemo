"""Fictional customer portal demo: no persistent accounts or real credentials."""
def register_customer(name: str, email: str) -> dict:
    name = name.strip()
    email = email.strip().lower()
    local, separator, domain = email.partition("@")
    if (not name or not separator or not local or not domain
            or "@" in domain or any(char.isspace() for char in email)
            or "." not in domain or any(not part for part in domain.split("."))):
        raise ValueError("Name and a valid email are required")
    return {"name": name, "email": email, "status": "registered"}


def dashboard_preferences(theme: str, page_size: int) -> dict:
    if theme not in {"light", "dark"} or page_size not in {10, 25, 50}:
        raise ValueError("Unsupported dashboard preference")
    return {"theme": theme, "page_size": page_size}
