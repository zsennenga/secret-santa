from flask import request

from app.blueprint.base_blueprint import BaseBlueprint
from app.db_session import db
from model.table.exchange_registration import SantaRegistration


class GiftExchange(BaseBlueprint):
    def __init__(self):
        super(GiftExchange, self).__init__(import_name=__name__, name='gift_exchange')

    def build_routes(self):
        @self.route('/', methods=['GET'])
        def home():
            # HTML page showing links to:
            # Summary Blurb
            # Register (if open)
            # View santa (if closed)
            return 'Hello, World!'

        @self.route('/register', methods=['POST'])
        def register_post():
            # TODO some kind of simple auth check
            what_to_get = request.form['what_to_get']
            what_not_to_get = request.form['what_not_to_get']
            who_to_ask_for_help = request.form['who_to_ask_for_help']

            registration = SantaRegistration(
                what_not_to_get=what_not_to_get,
                what_to_get=what_to_get,
                who_to_ask_for_help=who_to_ask_for_help
            )

            db.session.add(registration)
            db.session.commit()
