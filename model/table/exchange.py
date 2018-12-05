from __future__ import annotations

from datetime import datetime

from app.extensions.db_session import db


class Exchange(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    @classmethod
    def create(cls) -> Exchange:
        exchange = Exchange()

        db.session.add(exchange)
        db.session.commit()

        return exchange
