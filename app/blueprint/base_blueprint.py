from flask import Blueprint


class BaseBlueprint(Blueprint):
    def __init__(self, import_name, name, url_prefix=None):
        super(BaseBlueprint, self).__init__(
            import_name=import_name,
            name=name,
            url_prefix=url_prefix,
        )
        self.build_routes()

    def build_routes(self):
        raise NotImplementedError
