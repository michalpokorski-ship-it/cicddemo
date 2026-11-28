"""Fictional customer portal demo: no persistent accounts or real credentials."""
def register_customer(name: str, email: str) -> dict:
    name = name.strip()
    email = email.strip().lower()
    if not name or "@" not in email or not email.split("@", 1)[-1]:
        raise ValueError("Name and a valid email are required")
    return {"name": name, "email": email, "status": "registered"}
