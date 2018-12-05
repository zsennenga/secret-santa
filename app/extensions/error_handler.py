from exception.exchange_exception import ExchangeException
from model.service.logging_service import logging_service


class ErrorHandler:
    @classmethod
    def handle_500(cls, e: Exception):
        logging_service.logger.exception(e)
        if isinstance(e, ExchangeException):
            return str(e), e.response_code

        return e.__class__.__name__, 500
