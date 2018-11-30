import os

import pytest

from app.app import init_app
from app.config_base import ConfigBase
from app.db_session import db as _db
from config import Config


class ConfigTest(ConfigBase):
    DB_DRIVER = 'sqlite'
    DB_DATABASE = 'secret_santa'


@pytest.fixture(scope='session')
def app(request):
    app = init_app(
        import_name=__name__,
        config_module=ConfigTest
    )

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='session')
def db(request):
    """Session-wide test database."""
    db_path = f"/tmp/{Config.DB_DATABASE}"
    if os.path.exists(db_path):
        os.unlink(db_path)

    def teardown():
        _db.drop_all()
        os.unlink(db_path)

    request.addfinalizer(teardown)
    return _db


@pytest.fixture(scope='function')
def session(db, request):
    """Creates a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds={})
    session = db.create_scoped_session(options=options)

    db.session = session

    def teardown():
        transaction.rollback()
        connection.close()
        session.remove()

    request.addfinalizer(teardown)
    return session
