from typing import Type

from flask import Flask
from module_discovery_utils import load_all_modules_in_packages

from app.blueprint.auth import Auth
from app.blueprint.gift_exchange import GiftExchange
from app.blueprint.shared_pages import SharedPages
from app.extensions.db_session import db
from app.extensions.error_handler import ErrorHandler
from app.extensions.login_manager import login_manager
from app.extensions.reverse_proxied import ReverseProxied
from config import ConfigBase, Config
from model import table


def init_app(import_name: str, config_module: Type[ConfigBase]) -> Flask:
    app = Flask(import_name)
    app.wsgi_app = ReverseProxied(app.wsgi_app)

    app.config['SQLALCHEMY_DATABASE_URI'] = config_module.db_uri()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TEMPLATES_AUTO_RELOAD'] = True

    app.config['SERVER_NAME'] = config_module.SERVER_NAME

    app.secret_key = config_module.SECRET_KEY

    app.register_blueprint(SharedPages())
    app.register_blueprint(GiftExchange())
    app.register_blueprint(Auth())

    app.register_error_handler(Exception, ErrorHandler.handle_500)

    load_all_modules_in_packages(table)

    with app.app_context():
        db.init_app(app)
        db.create_all()

    login_manager.init_app(app)
    login_manager.login_view = "auth.login_get"

    return app


def init_default_app():
    return init_app(__name__, Config)
