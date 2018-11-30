from app.blueprint.base_blueprint import BaseBlueprint


class Auth(BaseBlueprint):
    def __init__(self):
        super(Auth, self).__init__(import_name=__name__, name='auth')

    def build_routes(self):
        @self.route('/login', methods=['GET'])
        def login_get():
            pass

        @self.route('/login', methods=['POST'])
        def login_post():
            pass

        @self.route('/register', methods=['GET'])
        def register_get():
            pass

        @self.route('/register', methods=['POST'])
        def register_post():
            pass
