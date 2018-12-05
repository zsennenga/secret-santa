from constant.exception_subtype import ExceptionSubtype
from exception.auth.auth_exception import AuthException


class NotLoggedIn(AuthException):
    def __init__(self):
        super(NotLoggedIn, self).__init__(
            subtype=ExceptionSubtype.ExceptionSubtype,
            message="Not logged in"
        )
