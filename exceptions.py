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

class UnprocessableEntityError(CropwiseAPIError):
    """Виняток, що виникає при некоректних даних у запиті."""
    pass

class DeletionNotAllowed(CropwiseAPIError):
    """Виняток, що виникає коли користувач не має прав на видалення ресурсу."""
    pass