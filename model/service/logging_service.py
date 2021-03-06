import logging

_logger = None


class LoggingService:
    @property
    def logger(self) -> logging.Logger:
        global _logger

        if _logger is None:
            _logger = logging.getLogger('secret_santa')

        return _logger


logging_service = LoggingService()
