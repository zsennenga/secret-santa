import random

from app.extensions.db_session import db
from exception.mapping.non_existent_exchange import NonExistentExchange
from model.service.logging_service import logging_service
from model.table.exchange import Exchange
from model.table.exchange_mapping import ExchangeMapping
from model.table.exchange_registration import ExchangeRegistration


class MatchingService:
    def _test_match(self, mappings):
        for giver, getter in mappings:
            if giver == getter:
                return False

        return True

    def _do_match(self, exchange_ids):
        while True:
            getter_registration_ids = exchange_ids.copy()
            random.shuffle(getter_registration_ids)

            mappings = list(zip(exchange_ids, getter_registration_ids))

            if not self._test_match(mappings):
                logging_service.logger.info("Failed to do match, recomputing..")
                continue

            return mappings

    def match_users(self, exchange_id):
        exchange = Exchange.get_by_id(exchange_id)
        if not exchange:
            raise NonExistentExchange(exchange_id)

        registrations = ExchangeRegistration.get_by_exchange_id(exchange_id)

        if len(registrations) <= 1:
            raise NotEnoughUsersToMatch()

        logging_service.logger.info(f"Matching {len(registrations)} users for {exchange_id}")

        mappings = self._do_match([element.id for element in registrations])

        for giver_registration_id, getter_registration_id in mappings:
            ExchangeMapping.setup_mapping(
                exchange_id=exchange_id,
                giver_registration_id=giver_registration_id,
                getter_registration_id=getter_registration_id,
            )

        db.session.commit()

        logging_service.logger.info(f"Matching complete for {exchange_id}")

