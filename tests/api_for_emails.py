import requests

from tests.value_provider import ValueProvider


class ApiForEmails:
    def __init__(self):
        self._hashed_email = None
        self._email = None
        self._payload = {}
        self._headers = {
            "apikey": ValueProvider.get_api_key_for_emails()
        }
        #  received from get_domains request as a rarely changed list
        #  to make less requests to api (limited to 500 per month)
        self._domain = [
            "@cevipsa.com",
            "@cpav3.com",
            "@nuclene.com",
            "@steveix.com",
            "@mocvn.com",
            "@tenvil.com",
            "@tgvis.com",
            "@amozix.com",
            "@anypsd.com",
            "@maxric.com"
        ]

    def generate_email(self):
        import random
        import string
        name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        domain = random.choice(self._domain)
        self._email = f"{name}{domain}"
        return self._email

    def get_hash_md5_of_email(self, email):
        import hashlib
        self._hashed_email = hashlib.md5(email.encode('utf-8')).hexdigest()
        return self._hashed_email

    def get_a_list_of_emails_for_a_mailbox(self, email):
        url = f"https://api.apilayer.com/temp_mail/mail/id/{self.get_hash_md5_of_email(email)}"
        response = requests.request("GET", url, headers=self._headers, data=self._payload)
        status_code = response.status_code
        result = response.text
        return status_code, result
