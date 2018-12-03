from enum import Enum


class ExceptionSubtype(Enum):
    UNABLE_TO_AUTHENTICATE = 'unable_to_authenticate'
    FIELD_MISSING = 'field_missing'
    DUPLICATE_EMAIL = 'duplicate_email'
