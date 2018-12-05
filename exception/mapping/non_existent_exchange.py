from constant.exception_subtype import ExceptionSubtype
from exception.exchange_exception import ExchangeException


class NonExistentExchange(ExchangeException):
    def __init__(self, exchange_id):
        super(NonExistentExchange, self).__init__(
            subtype=ExceptionSubtype.NOT_LOGGED_IN,
            message=f'Exchange {exchange_id} does not exist',
            response_code=400
        )
