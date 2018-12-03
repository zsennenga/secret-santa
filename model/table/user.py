from __future__ import annotations

from app.db_session import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(1024), nullable=False)
    name = db.Column(db.String(512), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    @classmethod
    def login(cls, email: str, password: str) -> User:
        # TODO for the love of god add a hashing algo here
        user = db.session(cls).filter(
            cls.email == email,
            cls.password == password
        ).first()

        if user is None:
            # TODO meaningful exception classes
            raise Exception('User not found with credentias')

        return user

    @classmethod
    def register(cls, email, password, name):
        new_user = User(
            email=email,
            password=password,
            name=name
        )

        db.session.add(new_user)
        db.session.commit()
