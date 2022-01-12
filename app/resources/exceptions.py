class BadAuthorizationException(Exception):
    def __init__(self, message: str = "Bad Authorization") -> None:
        self.__status_code = 403
    def get_status_code(self) -> int:
        return self.__status_code

class ResourceNotFoundException(Exception):
    def __init__(self, message: str = "Resource not found") -> None:
        self.__status_code = 404
    def get_status_code(self) -> int:
        return self.__status_code

class ResourceAlreadyExistsException(Exception):
    def __init__(self, message: str = "Resource already exists") -> None:
        self.__status_code = 409
    def get_status_code(self) -> int:
        return self.__status_code

class InvalidRequestException(Exception):
    def __init__(self, message: str = "Invalid json data") -> None:
        self.__status_code = 400
    def get_status_code(self) -> int:
        return self.__status_code

class UnauthorizedAccessException(Exception):
    def __init__(self, message: str = "You are not authorized to access to this resource") -> None:
        self.__status_code = 401
    def get_status_code(self) -> int:
        return self.__status_code

class InvalidEmailException(Exception):
    def __init__(self, message: str = "The provided email is invalid") -> None:
        self.__status_code = 500
    def get_status_code(self) -> int:
        return self.__status_code
