from exception.exchange_exception import ExchangeException


class ErrorHandler:
    @classmethod
    def handle_500(cls, e: Exception):
        if isinstance(e, ExchangeException):
            return str(e), e.response_code

        return e.__class__.__name__, 500
