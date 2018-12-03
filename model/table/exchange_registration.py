from app.extensions.db_session import db


class ExchangeRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exchange_id = db.Column(db.Integer, db.ForeignKey('exchange.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    what_to_get = db.Column(db.Text, nullable=False)
    what_not_to_get = db.Column(db.Text, nullable=False)
    who_to_ask_for_help = db.Column(db.Text, nullable=False)

