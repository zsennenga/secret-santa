from __future__ import annotations

from enum import Enum

from flask import url_for
from werkzeug.utils import redirect


class BlueprintName(Enum):
    AUTH = 'auth'
    ADMIN = 'admin'
    EXCHANGES = 'exchanges'
    SHARED = 'shared'

    def url_for(
            self,
            function_name: str,
            **kwargs
    ):
        return url_for(f'{self.value}.{function_name}', **kwargs)

    def redirect(
            self,
            function_name: str,
            **kwargs
    ):
        return redirect(self.url_for(function_name, **kwargs))
