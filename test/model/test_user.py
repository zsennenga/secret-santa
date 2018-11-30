from app.db_session import db
from model.table.user import User


def test_insert(app):
    user_model = User(
        email='test@test.com',
        password='test',
        name='test',
        is_admin='test',
    )

    with app.app_context():
        db.session.add(user_model)
        db.session.commit()

    assert user_model.id > 0
