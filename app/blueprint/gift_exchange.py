from flask import request, render_template
from flask_login import current_user, login_required

from app.blueprint.base_blueprint import BaseBlueprint
from app.extensions.db_session import db
from constant.blueprint_name import BlueprintName
from exception.auth.not_logged_in import NotLoggedIn
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
        @login_required
        def exchanges_get():
            return render_template('exchange/home.html')

        @self.route('/details/<id>', methods=['GET'])
        @login_required
        def details_get(id):
            return render_template('exchange/details.html')

        @self.route('/register', methods=['GET'])
        @login_required
        def exchange_register_get():
            return render_template('exchange/register.html')

        @self.route('/register', methods=['POST'])
        def exchange_register_post():
            if not current_user.is_authenticated:
                raise NotLoggedIn()
            exchange_id = request.form['id']
            what_to_get = request.form['what_to_get']
            what_not_to_get = request.form['what_not_to_get']
            who_to_ask_for_help = request.form['who_to_ask_for_help']

            registration = ExchangeRegistration(
                exchange_id=exchange_id,
                user_id=current_user.id,
                what_not_to_get=what_not_to_get,
                what_to_get=what_to_get,
                who_to_ask_for_help=who_to_ask_for_help,
            )

            db.session.add(registration)
            db.session.commit()
