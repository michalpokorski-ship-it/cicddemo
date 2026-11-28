import unittest
from unittest.mock import patch
from portal import register_customer, update_profile, recovery_confirmation, dashboard_preferences, dashboard_state, DemoSessions

class RegistrationTests(unittest.TestCase):
    def test_registration(self):
        self.assertEqual(register_customer(" Demo ", "USER@example.test"),
                         {"name": "Demo", "email": "user@example.test", "status": "registered"})

    def test_missing_name(self):
        with self.assertRaises(ValueError):
            register_customer("", "user@example.test")

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            register_customer("Demo", "invalid")

    def test_malformed_email_addresses(self):
        for email in ("@example.test", "user@@example.test", "user@example",
                      "u ser@example.test", "user@.test", "user@example..test"):
            with self.subTest(email=email):
                with self.assertRaises(ValueError):
                    register_customer("Demo", email)

    def test_profile_update(self):
        original = {"name": "Old", "email": "user@example.test"}
        self.assertEqual(update_profile(original, " New "), {"name": "New", "email": "user@example.test"})
        self.assertEqual(original["name"], "Old")
        with self.assertRaises(ValueError):
            update_profile(original, " ")

    def test_recovery_confirmation_is_generic(self):
        self.assertEqual(recovery_confirmation("known@example.test"), recovery_confirmation("unknown@example.test"))

    def test_dashboard_preferences(self):
        self.assertEqual(dashboard_preferences("dark", 25), {"theme": "dark", "page_size": 25})
        with self.assertRaises(ValueError):
            dashboard_preferences("unknown", 25)

    def test_dashboard_empty_state(self):
        self.assertEqual(dashboard_state([]), {"empty": True, "count": 0, "message": "No records yet"})
        self.assertFalse(dashboard_state([{"id": 1}])["empty"])

class SessionTests(unittest.TestCase):
    def test_session_lifecycle(self):
        sessions = DemoSessions()
        token = sessions.start("fictional-user")
        self.assertEqual(sessions.identity(token), "fictional-user")
        self.assertIsNone(sessions.identity("unknown"))
        self.assertNotEqual(token, sessions.start("fictional-user"))
        sessions.end(token)
        self.assertIsNone(sessions.identity(token))

    def test_expiry(self):
        sessions = DemoSessions(60)
        with patch("portal.time.monotonic", return_value=100):
            token = sessions.start("fictional-user")
        with patch("portal.time.monotonic", return_value=160):
            self.assertIsNone(sessions.identity(token))

if __name__ == "__main__":
    unittest.main()
