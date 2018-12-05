from constant.exception_subtype import ExceptionSubtype
from exception.auth.auth_exception import AuthException


class NotAuthorized(AuthException):
    def __init__(self):
        super(NotAuthorized, self).__init__(
            subtype=ExceptionSubtype.NOT_LOGGED_IN,
            message="Not authorized to perform this action"
        )
