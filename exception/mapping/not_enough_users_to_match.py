from constant.exception_subtype import ExceptionSubtype
from exception.exchange_exception import ExchangeException


class NotEnoughUsersToMatch(ExchangeException):
    def __init__(self):
        super(NotEnoughUsersToMatch, self).__init__(
            subtype=ExceptionSubtype.NOT_ENOUGH_USERS_TO_MATCH,
            message=f'Need more than 1 user to match',
            response_code=400
        )
