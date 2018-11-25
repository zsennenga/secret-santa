from flask import request

from app.santa import app, db
from models.santa_registration import SantaRegistration


@app.route('/')
def home():
    # HTML page showing links to:
    # Summary Blurb
    # Register (if open)
    # View santa (if closed)
    return 'Hello, World!'


@app.route('/register', methods=['GET'])
def register_get():
    # HTML form showing 5 things:
    # Name, email, what to get me, what not to get me, who to ask for help with my gift
    return ""


@app.route('/register', methods=['POST'])
def register_post():
    # TODO some kind of simple auth check
    email = request.form['email']
    name = request.form['name']
    what_to_get = request.form['what_to_get']
    what_not_to_get = request.form['what_not_to_get']
    who_to_ask_for_help = request.form['who_to_ask_for_help']

    registration = SantaRegistration(
        email=email,
        name=name,
        what_not_to_get=what_not_to_get,
        what_to_get=what_to_get,
        who_to_ask_for_help=who_to_ask_for_help
    )

    db.session.add(registration)
    db.session.commit()
