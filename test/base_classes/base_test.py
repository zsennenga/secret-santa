import os
import unittest

from app.app import init_app
from app.extensions.db_session import db
from config.config_test import Config


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
        ctx = app.test_request_context()
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
