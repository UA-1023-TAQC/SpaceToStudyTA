"""
https://apilayer.com/marketplace/temp_mail-api
"""
import json
import requests
import random
import string
import hashlib
import re

from tests.value_provider import ValueProvider
from bs4 import BeautifulSoup


def get_hashed_email(email):
    hashed_email = hashlib.md5(email.encode('utf-8')).hexdigest()
    return hashed_email


class TemporaryMailGenerator:
    #  received from get_domains request as a rarely changed list
    #  to make less requests to api (limited to 500 per month)
    domain = [
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

    # Used to get a new list of available domains from api
    # if the above domains are not available
    def get_domains(self):
        url = "https://api.apilayer.com/temp_mail/domains"
        response = requests.request("GET", url, headers=MailBox.headers, data=MailBox.payload)
        if response.status_code == 200:
            self.domain = json.loads(response.text)
            print(self.domain)
        return self.domain

    def generate_email_address(self, number_of_symbols=10):
        name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=number_of_symbols))
        domain = random.choice(self.get_domains())
        email_address = f"{name}{domain}"
        return email_address


class MailBox:
    payload = {}
    headers = {
        "apikey": ValueProvider.get_api_key_for_emails()
    }

    def __init__(self, email=None, hashed_email=None):
        self.email = email
        self.hashed_email = hashed_email
        self.letters = []

    def __str__(self):
        return f"{self.email} has {len(self.letters)} letters"

    def get_letters(self):
        url = f"https://api.apilayer.com/temp_mail/mail/id/{self.hashed_email}"
        response = requests.request("GET", url, headers=self.headers, data=self.payload)
        letter_data = response.json()
        if response.status_code == 200:
            if "error" in letter_data and letter_data["error"] == "There are no emails yet":
                self.letters = []
            else:
                self.letters = [Letter(letter) for letter in letter_data]
        else:
            self.letters = []
        return self.letters


class Letter:
    def __init__(self, data):
        self._id = data["_id"]["$oid"]
        self.created_at = data["createdAt"]["$date"]["$numberLong"]
        self.mail_address_id = data["mail_address_id"]
        self.mail_attachments = [Attachment(att_data) for att_data in data["mail_attachments"]]
        self.mail_attachments_count = data["mail_attachments_count"]
        self.mail_from = data["mail_from"]
        self.mail_html = data["mail_html"]
        self.mail_id = data["mail_id"]
        self.mail_preview = data["mail_preview"]
        self.mail_subject = data["mail_subject"]
        self.mail_text = data["mail_text"]
        self.mail_text_only = data["mail_text_only"]
        self.mail_timestamp = data["mail_timestamp"]

    def get_link_from_letter(self) -> str:
        letter_in_html = BeautifulSoup(self.mail_html, 'html.parser')
        link_element = letter_in_html.find('a', href=True)
        if link_element:
            link = link_element['href']
        else:
            link = None
        return link

    def get_sender_email(self) -> str:
        sender = self.mail_from
        email_pattern = r'<([^>]+)>'
        match = re.search(email_pattern, sender)
        if match:
            email = match.group(1)
        else:
            email = None
        return email


class Attachment:
    def __init__(self, data):
        self._id = data["_id"]
        self.cid = data["cid"]
        self.filename = data["filename"]
        self.mimetype = data["mimetype"]
        self.size = data["size"]
