from http.client import (
    FORBIDDEN, INTERNAL_SERVER_ERROR, METHOD_NOT_ALLOWED,
    NOT_FOUND, SERVICE_UNAVAILABLE, TOO_MANY_REQUESTS,
    UNAUTHORIZED, UNPROCESSABLE_ENTITY
)


class BaseRequestException(Exception):
    status_code = 400

    def __init__(self, message=None, *args: object, **kwargs: object) -> None:
        self.message = message or self.message
        super().__init__(*args, **kwargs)


class BadRequest(BaseRequestException):
    message = "Bad request"


class Forbidden(BaseRequestException):
    status_code = FORBIDDEN
    message = "You are not authorized to access this"


class InsufficientAmount(BaseRequestException):
    message = "Amount tendered is insufficient"


class MethodNotAllowed(BaseRequestException):
    status_code = METHOD_NOT_ALLOWED
    message = "Method not allowed"


class OperationException(BaseRequestException):
    status_code = INTERNAL_SERVER_ERROR
    message = "An error occured during this operation"


class RateLimitExceededException(BaseRequestException):
    status_code = TOO_MANY_REQUESTS
    message = "Rate limited exceeded"


class ResourceNotFound(BaseRequestException):
    status_code = NOT_FOUND
    message = "Not found"


class Unauthorized(BaseRequestException):
    status_code = UNAUTHORIZED
    message = "You are not permitted to access this"


class UnprocessableEntity(BaseRequestException):
    status_code = UNPROCESSABLE_ENTITY
    message = "More information required"


class UpstreamUnavailable(BaseRequestException):
    status_code = SERVICE_UNAVAILABLE
    message = "Something went wrong on our partner's end"
