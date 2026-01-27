import requests
from auth import Auth

class CropwiseClient:
    def __init__(self, email, password, base_url = None):
        self.base_url = base_url or "https://operations.cropwise.com/api/v3"
        self.auth = Auth(email, password, self.base_url)
        self.token = self.auth.login()

    def _headers(self):
        return {
            "X-User-Api-Token": f"{self.token}"
        }

    def _request(self, method, path, **kwargs):
        response = requests.request(method, self.base_url + path, headers=self._headers(), **kwargs)

        if response.status_code == 401:
          self.token = self.auth.login()
          response = requests.request(method, self.base_url + path, headers=self._headers(), **kwargs)

        return response.json()

    def get_fields(self):
        return self._request("GET", "/fields")