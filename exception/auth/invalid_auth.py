from constant.exception_subtype import ExceptionSubtype
from exception.auth.auth_exception import AuthException


class UnableToAuthenticate(AuthException):
    def __init__(self):
        super(UnableToAuthenticate, self).__init__(
            subtype=ExceptionSubtype.UNABLE_TO_AUTHENTICATE,
            message="Credentials don't match any user"
        )
