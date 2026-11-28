import unittest
from portal import register_customer, dashboard_state

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

    def test_dashboard_empty_state(self):
        self.assertEqual(dashboard_state([]), {"empty": True, "count": 0, "message": "No records yet"})
        self.assertFalse(dashboard_state([{"id": 1}])["empty"])

if __name__ == "__main__":
    unittest.main()
