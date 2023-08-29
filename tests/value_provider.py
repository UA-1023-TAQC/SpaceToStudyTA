import os

from dotenv import load_dotenv

load_dotenv()


class ValueProvider:
    @classmethod
    def get_student_email(cls) -> str:
        return os.getenv("STUDENT_EMAIL")

    @classmethod
    def get_student_password(cls) -> str:
        return os.getenv("STUDENT_PASSWORD")

    @classmethod
    def get_tutor_email(cls) -> str:
        return os.getenv("TUTOR_EMAIL")

    @classmethod
    def get_tutor_password(cls) -> str:
        return os.getenv("TUTOR_PASSWORD")

    @classmethod
    def get_base_url(cls) -> str:
        return os.getenv("BASE_URL")
