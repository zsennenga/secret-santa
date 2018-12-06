from datetime import datetime

from flask import render_template, request
from flask_login import current_user, login_required
from werkzeug.exceptions import NotFound, MethodNotAllowed
from werkzeug.utils import redirect

from app.blueprint.base_blueprint import BaseBlueprint
from app.forms import RegisterForm, CreateExchangeForm
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
        def exchanges_get():
            exchanges = Exchange.get_all()

            return render_template(
                'exchanges/list.html',
                exchanges=exchanges,
            )

        @self.route('/', methods=['POST'])
        @login_required
        def exchanges_post():
            exchange = Exchange.create(
                creator_id=current_user.id,
                name=request.form.get('name'),
                description=request.form.get('description'),
                ends_at=datetime.strptime(request.form.get('ends_at'), '%Y-%m-%d'),
            )
            return redirect(BlueprintName.EXCHANGES.url_for('exchange_get', friendly_id=exchange.friendly_id))

        @self.route('/create', methods=['GET'])
        @login_required
        def exchange_create_get():
            return render_template('exchanges/create.html', form=CreateExchangeForm())

        @self.route('/<friendly_id>', methods=['GET'])
        @login_required
        def exchange_get(friendly_id):
            exchange = Exchange.get_by_friendly_id(friendly_id)
            if not exchange:
                raise NotFound

            user_registration = ExchangeRegistration.get(exchange.id, current_user.id)

            match_registration = None
            if user_registration and user_registration.giver_mapping:
                match_registration = user_registration.giver_mapping.getter_registration

            return render_template(
                'exchanges/instance.html',
                exchange=exchange,
                your_registration=user_registration,
                match_registration=match_registration,
                form=RegisterForm(),
            )

        @self.route('/<friendly_id>/register', methods=['POST'])
        @login_required
        def exchange_register_post(friendly_id):
            exchange = Exchange.get_by_friendly_id(friendly_id)
            if not exchange:
                raise NotFound

            ExchangeRegistration.register(
                exchange_id=exchange.id,
                user_id=current_user.id,
                what_to_get=request.form.get('what_to_get'),
                what_not_to_get=request.form.get('what_not_to_get'),
                who_to_ask_for_help=request.form.get('who_to_ask_for_help'),
            )

            return redirect(BlueprintName.EXCHANGES.url_for('exchange_get', friendly_id=friendly_id))

        @self.route('/<friendly_id>/match', methods=['POST'])
        @login_required
        def match_post(friendly_id):
            exchange = Exchange.get_by_friendly_id(friendly_id)
            if not exchange:
                raise NotFound

            if current_user.id != exchange.creator_id:
                raise NotAuthorized

            if len(exchange.registered_user_ids) <= 1:
                raise MethodNotAllowed

            MatchingService().match_users(exchange.id)

            return redirect(BlueprintName.EXCHANGES.url_for('exchange_get', friendly_id=friendly_id))
