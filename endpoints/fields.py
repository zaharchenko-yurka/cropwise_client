class FieldsEndpoint:
    def __init__(self, client: 'CropwiseClient'):
        self.client = client

    def list(self, limit: int = 1000, from_id: int = 0) -> list:
        '''
        Отримує список полів користувача.

        :param limit: максимальна кількість полів для отримання
        :param from_id: початковий ID для пагінації
        '''
        return self.client._request("GET", "/fields", additional_headers={"limit": str(limit), "from_id": str(offset)})

    def get_single(self, field_id: int) -> dict:
        '''
        Отримує інформацію про конкретне поле за його ID.
        '''
        return self.client._request("GET", f"/fields/{field_id}")

    def list_of_ids(self) -> list:
        '''
        Отримує список усіх ID полів користувача.
        '''
        return self.client._request("GET", f"/fields/ids")
    
    def count(self) -> int:
        '''
        Отримує загальну кількість полів користувача.
        '''
        return self.client._request("GET", f"/fields/count")
    
    def create(self, data: dict) -> dict: #TODO: додавати {"data": {...}} до data
        '''
        Створює нове поле з наданими даними.
        '''
        return self.client._request("POST", "/fields", json=data)
    
    def update(self, field_id: int, data: dict) -> dict:  #TODO: додавати {"data": {...}} до data
        '''
        Оновлює інформацію про існуюче поле.
        '''
        return self.client._request("PUT", f"/fields/{field_id}", json=data)
    
    def delete(self, field_id: int) -> bool:
        '''
        Видаляє поле за його ID.
        '''
        return self.client._request("DELETE", f"/fields/{field_id}")

    def get_changes(self, from_time: str, to_time: str, to_time:) -> list:
        '''
        Отримує список змін полів з певного часу.

        :param from_time: початковий час у форматі ISO 8601
        :param to_time: кінцевий час у форматі ISO 8601
        '''
        return self.client._request("GET", f"/fields/changes", additional_headers={"From-Time": from_time, "To-Time": to_time})
    
    def get_changes_ids(self, from_time: str, to_time: str) -> list:
        '''
        Отримує список ID змінених полів в певний проміжок часу.

        :param from_time: початковий час у форматі ISO 8601
        :param to_time: кінцевий час у форматі ISO 8601
        '''
        return self.client._request("GET", f"/fields/changes_ids", additional_headers={"From-Time": from_time, "To-Time": to_time})

        # TODO: requesting of big number of objects