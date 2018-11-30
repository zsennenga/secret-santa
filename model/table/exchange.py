from datetime import datetime

from app.db_session import db


class Exchange(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.Datetime, default=datetime.utcnow, nullable=False)