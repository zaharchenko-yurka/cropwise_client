class OperationsEndpoint:
    def __init__(self, client):
        self.client = client

    def get_operations(self, field_id: int) -> dict:
        '''
        Отримує список операцій для заданого поля.

        :param field_id: Ідентифікатор поля
        :return: Словник з інформацією про операції
        '''
        return self.client._request("GET", "agro_operations?field_id={field_id}")
    
    def list(self):
        '''
        Отримує список всіх операцій.

        :return: Словник з інформацією про всі операції
        '''
        return self.client._request("GET", "/agro_operations")
    
    def planned(self):
        '''
        Отримує список запланованих операцій.

        :return: Словник з інформацією про заплановані операції
        '''
        return self.client._request("GET", "/agro_operations?status=planned")