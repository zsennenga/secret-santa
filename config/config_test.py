from config.config_base import ConfigBase


class Config(ConfigBase):
    DB_DRIVER = 'sqlite'
    DB_DATABASE = 'exchange_test'

    SECRET_KEY = 'buts lol'

    SERVER_NAME = '127.0.0.1'
