from datetime import datetime
from random import randint

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
        self.creator = User.register(
            email='test_email',
            plaintext_password='test_password',
            name='test_name'
        )

    def _rand(self):
        return randint(0, 10000000)

    def _create_exchange(self):
        return Exchange.create(
            creator_id=self.creator.id,
            name='test',
            ends_at=datetime.utcnow()
        )

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

    def _verify_match(self, exchange_id):
        registrations = ExchangeRegistration.get_by_exchange_id(exchange_id)
        mappings = ExchangeMapping.get_by_exchange_id(exchange_id)

        assert len(registrations) == len(mappings)

        user_ids = sorted(element.id for element in registrations)

        giver_registration_ids = sorted(element.giver_registration_id for element in mappings)
        getter_registration_ids = sorted(element.getter_registration_id for element in mappings)

        assert user_ids == giver_registration_ids == getter_registration_ids

    def test_many_exchange(self):
        for i in range(0, 10):
            exchange = self._create_exchange()

            for j in range(0, randint(2, 10)):
                self._create_user(exchange.id)

            self.match_service.match_users(exchange.id)

            self._verify_match(exchange.id)
