class FieldsEndpoint:
    def list(self) -> list:
        '''
        Отримує список полів користувача.

        :return: список об'єктів Field
        '''
        return self.client._request("GET", "/fields")
    
    def __init__(self, client: 'CropwiseClient'):
        self.client = client

    def get(self, field_id: int) -> dict:
        '''
        Отримує інформацію про конкретне поле за його ID.

        :param field_id: унікальний ідентифікатор поля
        :return: об'єкт Field
        '''
        return self.client._request("GET", f"/fields?id={field_id}")
