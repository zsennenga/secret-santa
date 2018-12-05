from datetime import datetime

from app.extensions.db_session import db


class ExchangeMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exchange_id = db.Column(db.Integer, db.ForeignKey('exchange.id'))
    giver_id = db.Column(db.Integer, db.ForeignKey('exchange_registration.id'), nullable=False)
    getter_id = db.Column(db.Integer, db.ForeignKey('exchange_registration.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    @classmethod
    def setup_mapping(cls, exchange_id, giver_id, getter_id):
        match = ExchangeMapping(
            exchange_id=exchange_id,
            giver_id=giver_id,
            getter_id=getter_id
        )

        db.session.add(match)

    @classmethod
    def get_by_exchange_id(cls, exchange_id):
        return db.session.query(ExchangeMapping).filter(
            cls.exchange_id == exchange_id
        ).all()
