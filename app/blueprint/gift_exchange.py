from datetime import datetime

from flask import render_template, request
from flask_login import current_user, login_required
from werkzeug.exceptions import NotFound
from werkzeug.utils import redirect

from app.blueprint.base_blueprint import BaseBlueprint
from app.forms import RegisterForm
from constant.blueprint_name import BlueprintName
from exception.auth.not_authorized import NotAuthorized
from model.service.matching_service import MatchingService
from model.table.exchange import Exchange
from model.table.exchange_registration import ExchangeRegistration


class GiftExchange(BaseBlueprint):
    def __init__(self):
        super(GiftExchange, self).__init__(
            import_name=__name__,
            name=BlueprintName.EXCHANGES.value,
            url_prefix='/exchanges'
        )

    def build_routes(self):
        @self.route('/', methods=['GET'])
        @login_required
        def exchanges_get():
            exchanges = Exchange.get_all()

            # XXX: If we don't have any exchanges, make one for testing
            if not exchanges:
                exchanges = [Exchange.create(
                    name='Secret Santa',
                    description='Gift a present to one of your closest friends on a day that is not Christmas!',
                    ends_at=datetime(2018, 12, 25),
                )]

            return render_template(
                'exchanges/home.html',
                exchanges=exchanges,
            )

        @self.route('/<id>', methods=['GET'])
        @login_required
        def exchange_get(id):
            exchange = Exchange.get_by_id(id)
            if not exchange:
                raise NotFound

            registration = ExchangeRegistration.get(id, current_user.id)

            return render_template(
                'exchanges/details.html',
                exchange=exchange,
                registration=registration,
            )

        @self.route('/<id>/register', methods=['GET'])
        @login_required
        def exchange_register_get(id):
            exchange = Exchange.get_by_id(id)
            if not exchange:
                raise NotFound

            return render_template(
                'exchanges/register.html',
                exchange=exchange,
                form=RegisterForm(),
            )

        @self.route('/<id>/register', methods=['POST'])
        @login_required
        def exchange_register_post(id):
            ExchangeRegistration.register(
                exchange_id=id,
                user_id=current_user.id,
                what_to_get=request.form.get('what_to_get'),
                what_not_to_get=request.form.get('what_not_to_get'),
                who_to_ask_for_help=request.form.get('who_to_ask_for_help'),
            )

            return redirect(BlueprintName.EXCHANGES.url_for('exchange_get', id=id))

        @self.route('/<id>/match', methods=['POST'])
        @login_required
        def match_post(id):
            if not current_user.is_admin:
                raise NotAuthorized()

            MatchingService().match_users(id)

            return redirect(BlueprintName.EXCHANGES.url_for('details_get', id=id))
