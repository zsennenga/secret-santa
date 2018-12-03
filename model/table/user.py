from __future__ import annotations

from app.extensions.db_session import db
from app.extensions.login_manager import login_manager
from exception.auth.duplicate_email import DuplicateEmail
from exception.auth.invalid_auth import UnableToAuthenticate
from model.service.auth_service import AuthService


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(256), unique=True, nullable=False)
    password = db.Column(db.String(1024), nullable=False)
    name = db.Column(db.String(512), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    @classmethod
    @login_manager.user_loader
    def get_by_id(cls, user_id: str):
        return db.session.query(User).filter(
            cls.id == user_id
        ).first()

    @classmethod
    def login(cls, email: str, plaintext_password: str) -> User:
        auth = AuthService()

        user = db.session.query(cls).filter(
            cls.email == email
        ).first()

        if user is None or not auth.verify_password(
                plaintext_password=plaintext_password,
                password_hash=user.password
        ):
            raise UnableToAuthenticate()

        return user

    @classmethod
    def register(cls, email: str, plaintext_password: str, name: str):
        existing_user = db.session.query(cls).filter(
            cls.email == email
        ).first()

        if existing_user:
            raise DuplicateEmail()

        auth = AuthService()

        new_user = User(
            email=email,
            password=auth.hash_password(plaintext_password=plaintext_password),
            name=name,
        )

        db.session.add(new_user)
        db.session.commit()

        return new_user

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)
