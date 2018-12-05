from __future__ import annotations

from datetime import datetime

from app.extensions.db_session import db
from constant.christmas_words import gen_phrase


class Exchange(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    friendly_identifier = db.Column(db.String(512))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    @classmethod
    def get_by_id(cls, exchange_id):
        return db.session.query(Exchange).filter(
            cls.id == exchange_id
        ).first()

    @classmethod
    def create(cls) -> Exchange:
        phrase = gen_phrase()

        while True:
            exchange = db.session.query(Exchange).filter(
                cls.friendly_identifier == phrase
            ).first()

            if not exchange:
                break

        exchange = Exchange(
            friendly_identifier=phrase
        )

        db.session.add(exchange)
        db.session.commit()

        return exchange
