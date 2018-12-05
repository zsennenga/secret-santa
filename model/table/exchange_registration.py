from __future__ import annotations

from datetime import datetime
from typing import Optional, List

from sqlalchemy.orm import relationship

from app.extensions.db_session import db


class ExchangeRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exchange_id = db.Column(db.Integer, db.ForeignKey('exchange.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    what_to_get = db.Column(db.Text, nullable=False)
    what_not_to_get = db.Column(db.Text, nullable=False)
    who_to_ask_for_help = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    exchange = relationship('Exchange', backref='registrations')
    user = relationship('User', backref='registrations')

    @classmethod
    def get(cls, exchange_id: int, user_id: int) -> Optional[ExchangeRegistration]:
        return db.session.query(ExchangeRegistration).filter(
            ExchangeRegistration.exchange_id == exchange_id,
            ExchangeRegistration.user_id == user_id,
        ).first()

    @classmethod
    def get_by_exchange_id(cls, exchange_id: int) -> List[ExchangeRegistration]:
        return db.session.query(ExchangeRegistration).filter(
            ExchangeRegistration.exchange_id == exchange_id
        ).all()

    @classmethod
    def register(
            cls,
            exchange_id: int,
            user_id: str,
            what_to_get: str,
            what_not_to_get: str,
            who_to_ask_for_help: str,
    ) -> ExchangeRegistration:
        registration = ExchangeRegistration(
            exchange_id=exchange_id,
            user_id=user_id,
            what_not_to_get=what_not_to_get,
            what_to_get=what_to_get,
            who_to_ask_for_help=who_to_ask_for_help,
        )

        db.session.add(registration)
        db.session.commit()

        return registration
