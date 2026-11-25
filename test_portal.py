import unittest
from portal import register_customer

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

if __name__ == "__main__":
    unittest.main()
