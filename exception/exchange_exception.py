from constant.exception_subtype import ExceptionSubtype


class ExchangeException(Exception):
    def __init__(
            self,
            subtype: ExceptionSubtype,
            message: str,
            response_code: int = 500,
    ):
        self.subtype = subtype
        self.message = message
        self.response_code = response_code

    def __str__(self):
        return f'[{self.__class__.__name__}] {str(self.subtype)}: {self.message}'
