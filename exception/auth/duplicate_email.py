from constant.exception_subtype import ExceptionSubtype
from exception.auth.auth_exception import AuthException


class DuplicateEmail(AuthException):
    def __init__(self):
        super(DuplicateEmail, self).__init__(
            subtype=ExceptionSubtype.DUPLICATE_EMAIL,
            message="Account with given email already exists",
            response_code=400,
        )
