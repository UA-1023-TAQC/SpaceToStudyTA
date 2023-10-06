import jwt


class BaseAPIClient:
    def __init__(self, url, accessToken=None):
        self.url = url
        self.accessToken = accessToken

    def get_decode_access_token(self) -> dict:
        if not self.accessToken:
            return None
        decoded = jwt.decode(self.accessToken, algorithms=["HS256"], options={"verify_signature": False})
        return decoded
