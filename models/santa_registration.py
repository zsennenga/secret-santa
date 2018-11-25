from app.santa import db


class SantaRegistration(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    what_to_get = db.Column(db.Text, nullable=False)
    what_not_to_get = db.Column(db.Text, nullable=False)
    who_to_ask_for_help = db.Column(db.Text, nullable=False)
