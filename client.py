import time
import requests
import logging
from auth import Auth
from endpoints.fields import FieldsEndpoint
from endpoints.operations import OperationsEndpoint
from exceptions import CropwiseAPIError, ServerError, PermissionDeniedError, NotFoundError, DeletionNotAllowed, UnprocessableEntityError

logger = logging.getLogger("cropwise_client")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

class CropwiseClient:
    '''
    Обгортка для взаємодії з Cropwise API згідно з документацією: https://cropwiseoperations.docs.apiary.io/
    '''
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

    def _request(self, method: str, path: str, retries: int = 3, **kwargs) -> dict:
        '''
        Заміна бібліотечного методу. Якщо сервер повертає 401, виконуємо повторний вхід.
        
        :param method: метод HTTP - GET, POST, і т.д.
        :param path: закінчення шляху API
        :param kwargs: додаткові параметри для requests.request
        '''
        
        for attempt in range(retries + 1):
            try:
                logger.info(f"Виконується {method} запит до {path}")
                response = requests.request(
                    method,
                    self.base_url + path,
                    headers=self._headers(method=method),
                    timeout=(5, 30),
                    **kwargs
                    )

                if response.status_code == 401:
                    logger.warning("Токен автентифікації недійсний або прострочений. Виконується повторний вхід.")
                    self.token = self.auth.login()
                    continue  # повторити запит після оновлення токена
                elif response.status_code == 302:
                    logger.warning(f"Видалення ресурсу цим користувачем заборонено.")
                    raise DeletionNotAllowed("Deletion not allowed.")
                elif response.status_code == 403:
                    logger.error("Доступ заборонено. Перевірте свої права доступу.")
                    raise PermissionDeniedError("Access denied.")
                elif response.status_code == 404:
                    logger.error("Ресурс не знайдено.")
                    raise NotFoundError("Resource not found.")
                elif response.status_code == 422:
                    logger.error("Некоректні дані у запиті.")
                    logger.error(f"Деталі: {response.text}")
                    raise UnprocessableEntityError("Unprocessable entity.")
                elif response.status_code in (500, 502, 503, 504):
                    logger.error(f"Помилка сервера: {response.status_code}")
                    raise ServerError(f"Server error: {response.status_code}")
                
                return response.json()
            except (requests.exceptions.Timeout, requests.exceptions.ConnectionError) as e:
                if attempt == retries:
                    raise CropwiseAPIError(f"Networking error: {str(e)}") from e
                logger.warning("Помилка мережі: %s. Спроба %d з %d.", str(e), attempt + 1, retries)
                time.sleep(2 ** attempt)  # експоненціальне збільшення затримки

