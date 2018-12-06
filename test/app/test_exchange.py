from datetime import datetime

from flask import Response

from constant.blueprint_name import BlueprintName
from model.table.exchange import Exchange
from model.table.exchange_registration import ExchangeRegistration
from model.table.user import User
from test.base_classes.base_test import BaseTest


class TestExchange(BaseTest):

    def setUp(self):
        super(TestExchange, self).setUp()
        self.what_to_get = 'a cat'
        self.what_not_to_get = 'a dog'
        self.who_to_ask_for_help = 'nora or zach'

        self.user = User.register(
            email='test_email',
            plaintext_password='test_password',
            name='test_name'
        )
        self.exchange = Exchange.create(
            creator_id=self.user.id,
            name='test',
            ends_at=datetime.utcnow()
        )

    def _register_request(
            self,
            friendly_id=None,
            user_id=None,
            what_to_get=None,
            what_not_to_get=None,
            who_to_ask_for_help=None
    ) -> Response:
        return self.client.post(
            BlueprintName.EXCHANGES.url_for(
                'exchange_register_post',
                friendly_id=friendly_id or self.exchange.friendly_id,
            ),
            data={

                'user_id': user_id or self.user.id,
                'what_to_get': what_to_get or self.what_to_get,
                'what_not_to_get': what_not_to_get or self.what_not_to_get,
                'who_to_ask_for_help': who_to_ask_for_help or self.who_to_ask_for_help
            }
        )

    def test_registration_logged_in(self):
        self.login_user()

        response = self._register_request()

        assert response.status_code == 302

        exchanges = self.db.session.query(ExchangeRegistration).all()

        assert len(exchanges) == 1

        exchange = exchanges[0]

        assert exchange.user_id == self.user.id
        assert exchange.what_to_get == self.what_to_get
        assert exchange.what_not_to_get == self.what_not_to_get
        assert exchange.who_to_ask_for_help == self.who_to_ask_for_help

    def test_registration_logged_out(self):
        response = self._register_request()

        assert response.status_code == 302

        assert self.db.session.query(ExchangeRegistration).count() == 0
