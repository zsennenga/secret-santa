from constant.exception_subtype import ExceptionSubtype
from exception.exchange_exception import ExchangeException


class AuthException(ExchangeException):
    def __init__(
            self,
            subtype: ExceptionSubtype,
            message: str,
            response_code: int = 401
    ):
        super(AuthException, self).__init__(
            subtype=subtype,
            message=message,
            response_code=response_code,
        )
