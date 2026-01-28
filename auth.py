import requests
import json
import os

class Auth:
    TOKEN_FILE = ".cashe/.cropwise_token.json"

    def __init__(self, email, password, base_url):
        self.base_url = base_url
        self.email = email
        self.password = password
        self.token = None

    def login(self):
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

        response = requests.post(url, data=payload, headers=headers)

        # DEBUG: лог відповіді
        if not response.ok:
            print("HTTP", response.status_code, "URL:", response.url)
            print("RESPONSE BODY:", response.text)

        response.raise_for_status()
        self.token = response.json().get("user_api_token")
        if not self.token:
            raise Exception("Token not found in response")
        self.save_token()
        return self.token

    def save_token(self):
        os.makedirs(os.path.dirname(self.TOKEN_FILE), exist_ok=True)
        with open(self.TOKEN_FILE, "w") as f:
            json.dump({"token": self.token}, f)

    def load_token(self):
        if os.path.exists(self.TOKEN_FILE):
            with open(self.TOKEN_FILE, "r") as f:
                data = json.load(f)
                self.token = data.get("token")
        return self.token