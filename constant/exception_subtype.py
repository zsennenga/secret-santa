from enum import Enum


class ExceptionSubtype(Enum):
    UNABLE_TO_AUTHENTICATE = 'unable_to_authenticate'
    FIELD_MISSING = 'field_missing'
    DUPLICATE_EMAIL = 'duplicate_email'
    NOT_LOGGED_IN = 'not_logged_in'
    NON_EXISTENT_EXCHANGE = 'non_existent_exchange'
    NOT_ENOUGH_USERS_TO_MATCH = 'not_enough_users_to_match'
