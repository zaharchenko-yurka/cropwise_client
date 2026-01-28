class CropwiseAPIError(Exception):
    """Базовий клас для всіх винятків Cropwise API."""
    pass

class NotFoundError(CropwiseAPIError):
    """Виняток, що виникає, коли ресурс не знайдено."""
    pass

class PermissionDeniedError(CropwiseAPIError):
    """Виняток, що виникає при відмові в доступі через недостатні права."""
    pass

class ServerError(CropwiseAPIError):
    """Виняток, що виникає при помилках на стороні сервера."""
    pass

class AuthenticationError(CropwiseAPIError):
    """Виняток, що виникає при проблемах автентифікації."""
    pass