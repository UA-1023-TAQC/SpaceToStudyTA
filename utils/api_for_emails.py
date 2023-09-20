import requests
import random
import string
import hashlib

from tests.value_provider import ValueProvider

'''
https://apilayer.com/marketplace/temp_mail-api
'''


class TemporaryMailAPI:
    def __init__(self):
        self.payload = {}
        self.headers = {
            "apikey": ValueProvider.get_api_key_for_emails()
        }


class TemporaryMailGenerator:

    def __init__(self):
        self._api = TemporaryMailAPI()
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
        name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
        domain = random.choice(self._domain)
        email = f"{name}{domain}"
        mailbox = MailBox()
        mailbox.email = email
        mailbox.hashed_email = self.get_hashed_email(email)
        return mailbox

    @staticmethod
    def get_hashed_email(email):
        hashed_email = hashlib.md5(email.encode('utf-8')).hexdigest()
        return hashed_email


class MailBox:

    def __init__(self):
        self.hashed_email = None
        self.email = None
        self._api = TemporaryMailAPI()

    def get_a_list_of_emails_for_a_mailbox(self):
        url = f"https://api.apilayer.com/temp_mail/mail/id/{self.hashed_email}"
        response = requests.request("GET", url, headers=self._api.headers, data=self._api.payload)
        status_code = response.status_code
        result = response.text
        return status_code, result


class Letter:
    pass
