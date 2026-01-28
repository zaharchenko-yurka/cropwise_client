import requests
import json
import os
import logging
from exceptions import AuthenticationError, PermissionDeniedError, NotFoundError, ServerError, CropwiseAPIError

logger = logging.getLogger("cropwise_auth")
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


class Auth:
    '''
    Docstring for Auth
    '''
    TOKEN_FILE = ".cashe/.cropwise_token.json"

    def __init__(self, email, password, base_url):
        self.base_url = base_url
        self.email = email
        self.password = password
        self.token = None

    def login(self, retries: int =3) -> str:
        token = self.load_token()
        if token:
            self.token = token
            return self.token
        
        url = f"{self.base_url}/sign_in"
        payload = json.dumps({
            "user_login": {
                "email": self.email,
                "password": self.password
            }
        })
        headers = {"Content-Type": "application/json"}

        for attempt in range(retries + 1):
            try:
                logger.info("Виконується вхід користувача %s.", self.email)
                response = requests.post(
                    url,
                    data=payload,
                    headers=headers,
                    timeout=10
                    )

                if response.status_code == 401:
                    logger.error("Невірні облікові дані для автентифікації.")
                    raise AuthenticationError("Authentication failed.")
                elif response.status_code == 403:
                    logger.error("Доступ заборонено. Перевірте свої права доступу.")
                    raise PermissionDeniedError("Access denied.")
                elif response.status_code ==404:
                    logger.error("Ресурс не знайдено.")
                    raise NotFoundError("Resource not found.")
                elif response.status_code in (500, 502, 503, 504):
                    logger.error(f"Помилка сервера: {response.status_code}")
                    raise ServerError(f"Server error: {response.status_code}")
                elif not response.ok:
                    logger.error(f"HTTP: {response.status_code}: {response.text}")
                    raise AuthenticationError(f"Authentication error: {response.status_code}")


                self.token = response.json().get("user_api_token")
                if not self.token:
                    logger.error("Token not found in response")
                    raise AuthenticationError("Token not found")
                self.save_token()
                return self.token
            except requests.exceptions.RequestException as e:
                if attempt == retries:
                    raise CropwiseAPIError(f"Networking error: {str(e)}") from e
                logger.warning("Помилка мережі: %s. Спроба %d з %d.", str(e), attempt + 1, retries)
                time.sleep(2 ** attempt)

    def save_token(self):
        os.makedirs(os.path.dirname(self.TOKEN_FILE), exist_ok=True)
        with open(self.TOKEN_FILE, "w", encoding="utf-8") as f:
            json.dump({"token": self.token}, f)

    def load_token(self):
        if os.path.exists(self.TOKEN_FILE):
            with open(self.TOKEN_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.token = data.get("token")
        return self.token