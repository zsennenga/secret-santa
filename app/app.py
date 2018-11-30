from typing import Type

from flask import Flask

from app.blueprint.auth import Auth
from app.blueprint.gift_exchange import GiftExchange
from app.blueprint.shared_pages import SharedPages
from app.config_base import ConfigBase
from app.db_session import db
from config import Config

_app: Flask = None


def init_app(import_name: str, config_module: Type[ConfigBase]) -> Flask:
    global _app

    if _app is not None:
        raise Exception('Multiple app initialization attempts!')

    _app = Flask(import_name)
    _app.config['SQLALCHEMY_DATABASE_URI'] = config_module.db_uri()

    _app.register_blueprint(SharedPages())

    _app.register_blueprint(GiftExchange(), url_prefix='/exchange')
    _app.register_blueprint(Auth(), url_prexfix='/auth')

    with _app.app_context():
        db.init_app(_app)
        db.create_all()

    return _app


def init_default_app():
    return init_app(__name__, Config)
