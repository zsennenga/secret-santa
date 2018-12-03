from constant.exception_subtype import ExceptionSubtype
from exception.exchange_exception import ExchangeException


class FieldMissing(ExchangeException):
    def __init__(
            self,
            field_name,
    ):
        super(FieldMissing, self).__init__(
            subtype=ExceptionSubtype.UNABLE_TO_AUTHENTICATE,
            message=f'Required field {field_name} missing',
            response_code=400
        )
