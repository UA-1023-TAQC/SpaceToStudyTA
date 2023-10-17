import jwt


class BaseAPIClient:
    def __init__(self, url, access_token=None):
        self.url = url
        self.access_token = access_token

    def get_decode_access_token(self) -> dict:
        decoded = {}
        if self.access_token:
            decoded = jwt.decode(self.access_token, algorithms=["HS256"], options={"verify_signature": False})
        return decoded
