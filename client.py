import requests
from auth import Auth
from endpoints.fields import FieldsEndpoint
from endpoints.operations import OperationsEndpoint

class CropwiseClient:
    def __init__(self, email, password, base_url = None):
        self.base_url = base_url or "https://operations.cropwise.com/api/v3"
        self.auth = Auth(email, password, self.base_url)
        self.token = self.auth.login()
        self.fields = FieldsEndpoint(self)
        self.operations = OperationsEndpoint(self)

    def _headers(self, method: str = "GET") -> dict:
        '''
        Повертає заголовки для запиту, включаючи токен автентифікації.

        :param method: метод HTTP - GET, POST, і т.д.
        :return: заголовки для запиту
        '''
        headers = {"Content-Type": "application/json"} if method in ["POST", "PUT"] else {}
        headers.update({"X-User-Api-Token": f"{self.token}"})
        return headers

    def _request(self, method: str, path: str, **kwargs) -> dict:
        '''
        Заміна бібліотечного методу. Якщо сервер повертає 401, виконуємо повторний вхід.
        
        :param method: метод HTTP - GET, POST, і т.д.
        :param path: закінчення шляху API
        :param kwargs: додаткові параметри для requests.request
        '''
        response = requests.request(method, self.base_url + path, headers=self._headers(method=method), timeout=30, **kwargs)

        if response.status_code == 401:
          self.token = self.auth.login()
          response = requests.request(method, self.base_url + path, headers=self._headers(method=method), timeout=30, **kwargs)
        
        response.raise_for_status()
        return response.json()

    def get_fields(self):
        return self._request("GET", "/fields")