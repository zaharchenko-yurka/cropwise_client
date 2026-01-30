class ReadOnlyEndpoint:
    resource = ""

    def __init__(self, client: 'CropwiseClient'):
        self.client = client

    def list(self, limit: int = 1000, from_id: int = 0) -> list:
        '''
        Отримує список об'єктів користувача.

        :param limit: максимальна кількість об'єктів для отримання
        :param from_id: початковий ID для пагінації
        '''
        return self.client._request("GET", f"/{self.resource}", additional_headers={"limit": str(limit), "from_id": str(from_id)})

    def get_single(self, field_id: int) -> dict:
        '''
        Отримує інформацію про конкретний об'єкт за його ID.
        '''
        return self.client._request("GET", f"/{self.resource}/{field_id}")

    def list_of_ids(self) -> list:
        '''
        Отримує список усіх ID об'єктів користувача.
        '''
        return self.client._request("GET", f"/{self.resource}/ids")
    
    def count(self) -> int:
        '''
        Отримує загальну кількість об'єктів користувача.
        '''
        return self.client._request("GET", f"/{self.resource}/count")
    
    def get_changes(self, from_time: str, to_time: str, to_time:) -> list:
        '''
        Отримує список змін об'єктів з певного часу.
        :param from_time: початковий час у форматі ISO 8601
        :param to_time: кінцевий час у форматі ISO 8601
        '''
        return self.client._request("GET", f"/{self.resource}/changes", additional_headers={"From-Time": from_time, "To-Time": to_time})
    
    def get_changes_ids(self, from_time: str, to_time: str) -> list:
        '''
        Отримує список ID змінених об'єктів в певний проміжок часу.
        :param from_time: початковий час у форматі ISO 8601
        :param to_time: кінцевий час у форматі ISO 8601
        '''
        return self.client._request("GET", f"/{self.resource}/changes_ids", additional_headers={"From-Time": from_time, "To-Time": to_time})
    def mass_request(self, ids: list) -> list:
        '''
        Виконує масовий запит для отримання інформації про кілька об'єктів за їх ID.
        :param ids: список ID об'єктів
        '''
        return self.client._request("POST", f"/{self.resource}/mass_request", additional_headers={"data": ids})
    
class BaseEndpoint(ReadOnlyEndpoint):
    def create(self, data: dict) -> dict:
        '''
        Створює новий об'єкт з наданими даними.
        '''
        return self.client._request("POST", f"/{self.resource}", additional_headers={"data": data})
    
    def update(self, field_id: int, data: dict) -> dict:
        '''
        Оновлює інформацію про існуючий об'єкт.
        '''
        return self.client._request("PUT", f"/{self.resource}/{field_id}", additional_headers={"data": data})
    
    def delete(self, field_id: int) -> bool:
        '''
        Видаляє об'єкт за його ID.
        '''
        return self.client._request("DELETE", f"/{self.resource}/{field_id}")
