class ConfigBase:
    DB_DRIVER = ''
    DB_HOST = ''
    DB_DATABASE = ''
    DB_USER = ''
    DB_PASS = ''

    SECRET_KEY = None

    SERVER_NAME = None

    @classmethod
    def db_uri(cls):
        if cls.DB_DRIVER == 'mysql':
            return f'mysql://{cls.DB_USER}:{cls.DB_PASS}@{cls.DB_HOST}/{cls.DB_DATABASE}'
        elif cls.DB_DRIVER == 'sqlite':
            return f'sqlite:////tmp/{cls.DB_DATABASE}'
        else:
            raise Exception(f'Invalid DB Driver: {cls.DB_DRIVER}')
