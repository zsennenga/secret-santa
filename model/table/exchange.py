from __future__ import annotations

from datetime import datetime
from typing import List

from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship

from app.extensions.db_session import db
from constant.christmas_words import gen_phrase


class Exchange(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    friendly_id = db.Column(db.String(512))
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text)
    ends_at = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    creator = relationship('User', backref='created_exchanges')
    registered_user_ids = association_proxy('registrations', 'user_id')

    @classmethod
    def get_by_id(cls, exchange_id):
        return db.session.query(Exchange).filter(
            cls.id == exchange_id
        ).first()

    @classmethod
    def get_by_friendly_id(cls, friendly_id: str):
        return db.session.query(Exchange).filter(
            cls.friendly_id == friendly_id
        ).first()

    @classmethod
    def create(cls, creator_id: int, name: str, ends_at: datetime, description: str=None) -> Exchange:
        phrase = gen_phrase()

        # Generate a unique phrase to use as an opaque token
        while True:
            exchange = db.session.query(Exchange).filter(
                cls.friendly_id == phrase
            ).first()

            if not exchange:
                break

            phrase = gen_phrase()

        exchange = Exchange(
            creator_id=creator_id,
            name=name,
            friendly_id=phrase,
            description=description,
            ends_at=ends_at,
        )

        db.session.add(exchange)
        db.session.commit()

        return exchange

    @classmethod
    def get_all(cls) -> List[Exchange]:
        return db.session.query(cls).all()
