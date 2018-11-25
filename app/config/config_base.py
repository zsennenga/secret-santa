class ConfigBase:
    REGISTRATION_OPEN = True

    DB_HOST = ''
    DB_DATABASE = ''
    DB_USER = ''
    DB_PASS = ''

    @classmethod
    def db_uri(cls):
        return ''
