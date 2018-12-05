from __future__ import annotations

from enum import Enum

from flask import url_for


class BlueprintName(Enum):
    AUTH = 'auth'
    ADMIN = 'admin'
    EXCHANGE = 'exchange'
    SHARED = 'shared'

    def url_for(
            self,
            function_name: str,
            **kwargs
    ):
        return url_for(f'{self.value}.{function_name}', **kwargs)
