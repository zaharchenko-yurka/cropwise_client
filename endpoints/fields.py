class FieldsEndpoint:
    def list(self) -> list:
        '''
        Отримує список полів користувача.

        :return: список об'єктів Field
        '''
        return self.client._request("GET", "/fields")
    
    def __init__(self, client: 'CropwiseClient'):
        self.client = client

    def get_single(self, field_id: int) -> dict:
        '''
        Отримує інформацію про конкретне поле за його ID.

        :param field_id: унікальний ідентифікатор поля
        :return: об'єкт Field
        '''
        return self.client._request("GET", f"/fields/{field_id}")

    def list_of_ids(self) -> list:
        return self.client._request("GET", f"/fields/ids")
    
    def count(self) -> int:
        return self.client._request("GET", f"/fields/count")
    
    def create(self, data: dict) -> dict:
        '''
        Створює нове поле з наданими даними.

        :param data: словник з інформацією про поле
        :return: об'єкт створеного Field
        '''
        return self.client._request("POST", "/fields", json=data)
    
    def update(self, field_id: int, data: dict) -> dict:
        '''
        Оновлює інформацію про існуюче поле.

        :param field_id: унікальний ідентифікатор поля
        :param data: словник з оновленою інформацією про поле
        :return: об'єкт оновленого Field
        '''
        return self.client._request("PUT", f"/fields/{field_id}", json=data)
    
    def delete(self, field_id: int) -> None:
        '''
        Видаляє поле за його ID.

        :param field_id: унікальний ідентифікатор поля
        '''
        self.client._request("DELETE", f"/fields/{field_id}")

    def 