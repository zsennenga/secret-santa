from flask import Blueprint
from flask_login import current_user


class BaseBlueprint(Blueprint):
    def __init__(self, import_name, name, url_prefix=None):
        super(BaseBlueprint, self).__init__(
            import_name=import_name,
            name=name,
            url_prefix=url_prefix,
        )
        self.build_globals()
        self.build_routes()

    def build_globals(self):
        @self.context_processor
        def preload_context():
            return {'user': current_user}

    def build_routes(self):
        raise NotImplementedError
