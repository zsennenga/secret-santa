from flask import url_for


class BlueprintName:
    AUTH = 'auth'
    ADMIN = 'admin'
    EXCHANGE = 'exchange'
    SHARED = 'shared'

    def url_for(self, blueprint, function_name):
        return url_for(f'{blueprint}.{function_name}')
