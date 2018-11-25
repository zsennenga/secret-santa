from app.santa import db


class SantaMapping(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    giver_id = db.Column(db.Integer, db.ForeignKey('santa_registration.id'), unique=True, nullable=False)
    getter_id = db.Column(db.Integer, db.ForeignKey('santa_registration.id'), unique=True, nullable=False)
