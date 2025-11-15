import unittest
from problem_7 import validate_email
from problem_7 import DOMAIN_CHARACTER_LIMIT


class TestValidateEmail(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(validate_email("johndoe@domainsample.com"))
        self.assertTrue(validate_email("john.doe@domainsample.net"))
        self.assertTrue(validate_email("john.doe43@domainsample.co.uk"))
        self.assertTrue(validate_email("john.doe+spamfilter@domainsample.co.uk"))

    def test_invalid_emails(self):
        self.assertFalse(validate_email("@domainsample.com"))
        self.assertFalse(validate_email("johndoedomainsample.com"))
        self.assertFalse(validate_email("john.doe@.net"))
        self.assertFalse(validate_email("john.doe43@domainsample"))

    def test_domain_exceeds_character_limit(self):
        long_domain = "a" * DOMAIN_CHARACTER_LIMIT
        email = f"test@{long_domain}.com"
        self.assertFalse(validate_email(email))

    def test_dot_immediately_after_at(self):
        self.assertFalse(validate_email("johndoe@.domainsample.com"))

    def test_multiple_at_symbols(self):
        self.assertFalse(validate_email("john@doe@domainsample.com"))

    def test_empty_string(self):
        self.assertFalse(validate_email(""))

    def test_domain_at_exact_limit(self):
        domain = "a" * 240 + ".com"
        email = f"test@{domain}"
        self.assertTrue(validate_email(email))


if __name__ == "__main__":
    unittest.main()
