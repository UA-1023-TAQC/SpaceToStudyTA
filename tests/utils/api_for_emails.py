"""
https://apilayer.com/marketplace/temp_mail-api
"""
import hashlib
import json
import requests
import random
import re
import string

from time import sleep

from bs4 import BeautifulSoup

from tests.utils.value_provider import ValueProvider


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
        response = requests.request("GET", url, headers=ValueProvider.get_api_key_for_emails(), data={})
        if response.status_code == 200:
            self.domain = json.loads(response.text)
        return self.domain

    def generate_email_address(self, number_of_symbols=10):
        name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=number_of_symbols))
        domain = random.choice(self.domain)
        email_address = f"{name}{domain}"
        return email_address


class MailBox:
    def __init__(self, email):
        self.payload = {}
        self.headers = {
            "apikey": ValueProvider.get_api_key_for_emails()
        }
        self.email = email
        self.hashed_email = get_hashed_email(email)
        self.letters = []

    def __str__(self):
        return f"{self.email} has {len(self.letters)} letters"

    def get_letters(self):
        url = f"https://api.apilayer.com/temp_mail/mail/id/{self.hashed_email}"
        letter_data = {'error': "There are no emails yet"}
        counter = 0

        while counter <= 10 and "error" in letter_data and letter_data["error"] == "There are no emails yet":
            response = requests.request("GET", url, headers=self.headers, data=self.payload)
            print(f"response code_________{response.status_code}")
            letter_data = response.json()
            counter += 1
            sleep(1)

        self.letters = [Letter(letter) for letter in letter_data] if "error" not in letter_data else []
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
        link = link_element['href'] if link_element else None
        return link

    def get_sender_email(self) -> str:
        sender = self.mail_from
        email_pattern = r'<([^>]+)>'
        matched_email = re.search(email_pattern, sender)
        email = matched_email.group(1) if matched_email else None
        return email


class Attachment:
    def __init__(self, data):
        self._id = data["_id"]
        self.cid = data["cid"]
        self.filename = data["filename"]
        self.mimetype = data["mimetype"]
        self.size = data["size"]
