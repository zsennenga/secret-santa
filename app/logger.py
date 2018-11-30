import logging

_logger: logging.Logger = None


def logger() -> logging.Logger:
    global _logger

    if _logger is None:
        _logger = logging.getLogger('secret_santa')

    return _logger
