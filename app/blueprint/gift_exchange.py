from flask import request, render_template

from app.blueprint.base_blueprint import BaseBlueprint
from app.extensions.db_session import db
from constant.blueprint_name import BlueprintName
from model.table.exchange_registration import ExchangeRegistration


class GiftExchange(BaseBlueprint):
    def __init__(self):
        super(GiftExchange, self).__init__(
            import_name=__name__,
            name=BlueprintName.EXCHANGE.value,
            url_prefix='/exchange'
        )

    def build_routes(self):
        @self.route('/', methods=['GET'])
        def home():
            # HTML page showing links to:
            # Summary Blurb
            # Register (if open)
            # View santa (if closed)
            return render_template('exchange/home.html')

        @self.route('/register', methods=['POST'])
        def register_post():
            # TODO some kind of simple auth check
            what_to_get = request.form['what_to_get']
            what_not_to_get = request.form['what_not_to_get']
            who_to_ask_for_help = request.form['who_to_ask_for_help']

            registration = ExchangeRegistration(
                what_not_to_get=what_not_to_get,
                what_to_get=what_to_get,
                who_to_ask_for_help=who_to_ask_for_help
            )

            db.session.add(registration)
            db.session.commit()
