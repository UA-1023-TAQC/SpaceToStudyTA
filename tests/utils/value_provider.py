import os

from dotenv import load_dotenv
from pathlib import Path


load_dotenv()


class ValueProvider:
    @classmethod
    def get_student_email(cls) -> str:
        return os.getenv("STUDENT_EMAIL")

    @classmethod
    def get_student_password(cls) -> str:
        return os.getenv("STUDENT_PASSWORD")

    @classmethod
    def get_student_first_name(cls) -> str:
        return os.getenv("STUDENT_FIRST_NAME")

    @classmethod
    def get_student_last_name(cls) -> str:
        return os.getenv("STUDENT_LAST_NAME")

    @classmethod
    def get_tutor_email(cls) -> str:
        return os.getenv("TUTOR_EMAIL")

    @classmethod
    def get_tutor_password(cls) -> str:
        return os.getenv("TUTOR_PASSWORD")

    @classmethod
    def get_tutor_first_name(cls) -> str:
        return os.getenv("TUTOR_FIRST_NAME")

    @classmethod
    def get_tutor_last_name(cls) -> str:
        return os.getenv("TUTOR_LAST_NAME")

    @classmethod
    def get_base_url(cls) -> str:
        return os.getenv("BASE_URL")

    @classmethod
    def get_api_key_for_emails(cls) -> str:
        return os.getenv("API_KEY_FOR_EMAILS")

    @classmethod
    def get_base_api_url(cls) -> str:
        return os.getenv("BASE_API_URL")

    @classmethod
    def get_built_test_data_file_path(cls, name) -> str:
        return os.path.join(Path(__file__).parent.parent, "data", name)
