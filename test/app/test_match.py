from random import randint

from flask import Response

from constant.blueprint_name import BlueprintName
from model.service.matching_service import MatchingService
from model.table.exchange import Exchange
from model.table.exchange_mapping import ExchangeMapping
from model.table.exchange_registration import ExchangeRegistration
from model.table.user import User
from test.base_classes.base_test import BaseTest


class TestMatch(BaseTest):
    def setUp(self):
        super(TestMatch, self).setUp()
        self.match_service = MatchingService()

    def _rand(self):
        return randint(0, 10000000)

    def _create_exchange(self):
        return Exchange.create()

    def _create_user(self, exchange_id):
        user = User.register(
            email=f"{self._rand()}.{self._rand()}.{self._rand()}.{self._rand()}",
            name="name",
            plaintext_password="password",
        )

        ExchangeRegistration.register(
            exchange_id=exchange_id,
            user_id=user.id,
            who_to_ask_for_help='',
            what_not_to_get='',
            what_to_get='',
        )

        return user

    def _verify_match(self, exchange_id):
        registrations = ExchangeRegistration.get_by_exchange_id(exchange_id)
        mappings = ExchangeMapping.get_by_exchange_id(exchange_id)

        assert len(registrations) == len(mappings)

        user_ids = sorted(element.id for element in registrations)

        giver_ids = sorted(element.giver_id for element in mappings)
        getter_ids = sorted(element.getter_id for element in mappings)

        assert user_ids == giver_ids == getter_ids

    def _register_request(
            self,
            exchange_id=None,
    ) -> Response:
        return self.client.post(
            BlueprintName.EXCHANGES.url_for('match_post', id=exchange_id)
        )

    def test_exchange_not_admin(self):
        exchange = self._create_exchange()
        user = self._create_user(exchange.id)
        self._create_user(exchange.id)

        self.login_user(email=user.email, password='password')

        response = self._register_request(exchange.id)

        assert response.status_code == 401

    def test_exchange_is_admin(self):
        exchange = self._create_exchange()
        user = self._create_user(exchange.id)
        self._create_user(exchange.id)

        user.is_admin = True
        self.db.session.commit()

        self.login_user(email=user.email, password='password')

        response = self._register_request(exchange.id)

        assert response.status_code == 302

        self._verify_match(exchange.id)
