import random

from app.extensions.db_session import db
from model.table.exchange import Exchange
from model.table.exchange_mapping import ExchangeMapping
from model.table.exchange_registration import ExchangeRegistration


class MatchingService:
    def _test_match(self, mappings):
        for giver, getter in mappings:
            if giver == getter:
                return False

        return True

    def _do_match(self, user_ids):
        giver_ids = user_ids

        while True:
            getter_ids = user_ids.copy()
            random.shuffle(getter_ids)

            mappings = list(zip(giver_ids, getter_ids))

            if not self._test_match(mappings):
                continue

            return mappings

    def match_users(self, exchange_id):
        exchange = Exchange.get_by_id(exchange_id)
        if not exchange:
            raise Exception

        registrations = ExchangeRegistration.get_by_exchange_id(exchange_id)

        if len(registrations) in (0, 1):
            raise Exception

        mappings = self._do_match([element.id for element in registrations])

        for giver_id, getter_id in mappings:
            ExchangeMapping.setup_registration(
                exchange_id=exchange_id,
                giver_id=giver_id,
                getter_id=getter_id,
            )

        db.session.commit()
