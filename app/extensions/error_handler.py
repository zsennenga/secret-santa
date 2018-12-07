from flask import flash
from werkzeug.utils import redirect

from constant.blueprint_name import BlueprintName
from model.service.logging_service import logging_service


class ErrorHandler:
    @classmethod
    def handle_500(cls, e: Exception):
        logging_service.logger.exception(e)
        flash(str(e), 'error')
        return BlueprintName.SHARED.redirect('home_get')
