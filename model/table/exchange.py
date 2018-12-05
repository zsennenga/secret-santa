from __future__ import annotations

from datetime import datetime
from typing import List

from app.extensions.db_session import db
from constant.christmas_words import gen_phrase


class Exchange(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    friendly_identifier = db.Column(db.String(512))
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    ends_at = db.Column(db.DateTime, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    @classmethod
    def get_by_id(cls, exchange_id):
        return db.session.query(Exchange).filter(
            cls.id == exchange_id
        ).first()

    @classmethod
    def get_by_id(cls, exchange_id: int):
        return db.session.query(Exchange).filter(
            cls.id == exchange_id
        ).first()

    @classmethod
    def create(cls, name: str, ends_at: datetime, description: str=None) -> Exchange:
        phrase = gen_phrase()

        # Generate a unique phrase to use as an opaque token
        while True:
            exchange = db.session.query(Exchange).filter(
                cls.friendly_identifier == phrase
            ).first()

            if not exchange:
                break

            phrase = gen_phrase()

        exchange = Exchange(
            name=name,
            friendly_identifier=phrase,
            description=description,
            ends_at=ends_at,
        )

        db.session.add(exchange)
        db.session.commit()

        return exchange

    @classmethod
    def get_all(cls) -> List[Exchange]:
        return db.session.query(cls).all()
