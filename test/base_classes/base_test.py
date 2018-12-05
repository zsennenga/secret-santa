import os
import unittest

from flask import Response, _request_ctx_stack
from flask_login import current_user

from app.app import init_app
from app.extensions.db_session import db
from config.config_test import Config
from constant.blueprint_name import BlueprintName

class BaseTest(unittest.TestCase):
    app = None
    client = None

    db_path = None
    db = None

    @classmethod
    def _build_db(cls, db_path):
        """Session-wide test database."""
        if os.path.exists(db_path):
            os.unlink(db_path)

        return db

    @classmethod
    def _build_app(cls):
        app = init_app(
            import_name=__name__,
            config_module=Config
        )

        # Establish an application context before running the tests.
        ctx = app.app_context()
        ctx.push()

        return app

    @classmethod
    def setUpClass(cls):
        cls.app = cls._build_app()
        cls.client = cls.app.test_client()

        cls.db_path = os.path.abspath(f"tmp/{Config.DB_DATABASE}")
        cls.db = cls._build_db(cls.db_path)

    @classmethod
    def tearDownClass(cls):
        cls.db.drop_all()
        if os.path.exists(cls.db_path):
            os.unlink(cls.db_path)

    def setUp(self):
        self.db.create_all()

    def tearDown(self):
        self.db.drop_all()
        self.client.cookie_jar.clear()

    def register_post(self, email=None, password=None, name=None) -> Response:
        return self.client.post(
            BlueprintName.AUTH.url_for('register_post'),
            data={
                'email': email or 'test_email',
                'password': password or 'test_password',
                'name': name or 'test_name'
            }
        )

    def login_user(self, email=None, password=None) -> Response:
        return self.client.post(
            BlueprintName.AUTH.url_for('login_post'),
            data={
                'email': email or 'test_email',
                'password': password or 'test_password'
            }
        )
