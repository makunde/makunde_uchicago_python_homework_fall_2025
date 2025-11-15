"""Write a robust email validation function that takes a string as a parameter
and returns True if it is a valid email. Return False if it is not valid.

A valid email address has four parts:

Recipient name
@ symbol
Domain name
Top-level domain
The parts are ordered as follows:

recipient_name@domain_name.top_level_domain
The recipient name may be a maximum of 64 characters long and consist of:

Uppercase and lowercase letters in English (A-Z, a-z)
Digits from 0 to 9
Special characters: the period (.), underscore(_), hyphen (-) and plus sign (+)
The domain name is a string of letters and digits that defines a space on the
Internet owned and controlled by a specific mailbox provider or organization.

Domain names may be a maximum of 253 characters and consist of:
Uppercase and lowercase letters in English (A-Z, a-z)
Digits from 0 to 9
A hyphen "-"
A period "." (used to identify a sub-domain; for example, email.domainsample)
Top-level domains are the highest level of the domain name system for the Internet and is placed after the domain name in an email address.

Common top-level domains are:

.com
.net
.org
"""

import re
import sys

DOMAIN_CHARACTER_LIMIT = 253


def validate_email(email):
    valid_email_pattern = re.compile(
        r"^([a-zA-Z0-9\.\-_+]+)@([a-zA-Z0-9\-_]+\.?[a-zA-Z0-9\-_]*\.[a-zA-Z]+)$"
    )
    matches = valid_email_pattern.findall(email)
    match_found = False
    print(matches)
    if len(matches) > 0:
        domain = matches[0][1]
        if len(domain) <= DOMAIN_CHARACTER_LIMIT:
            match_found = True
    return match_found


def main():
    emails = sys.argv[1:]
    for email in emails:
        validate_email(email)


if __name__ == "__main__":
    main()
