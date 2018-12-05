from flask import Response

from constant.blueprint_name import BlueprintName
from model.table.exchange import Exchange
from model.table.user import User
from test.base_classes.base_test import BaseTest


class TestExchange(BaseTest):

    def setUp(self):
        super(TestExchange, self).setUp()
        self.what_to_get = 'a cat'
        self.what_not_to_get = 'a dog'
        self.who_to_ask_for_help = 'nora or zach'

        self.exchange = Exchange.create()
        self.user = User.register(
            email='test_email',
            plaintext_password='test_password',
            name='test_name'
        )

    def _register_request(
            self,
            exchange_id=None,
            user_id=None,
            what_to_get=None,
            what_not_to_get=None,
            who_to_ask_for_help=None
    ) -> Response:
        return self.client.post(
            BlueprintName.EXCHANGE.url_for('exchange_register_post', id=exchange_id or self.exchange.id),
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

        assert response.status_code == 200
