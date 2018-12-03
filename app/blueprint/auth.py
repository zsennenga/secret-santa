from flask import request, render_template, url_for
from werkzeug.utils import redirect

from app.blueprint.base_blueprint import BaseBlueprint
from constant.blueprint_name import BlueprintName
from model.table.user import User


class Auth(BaseBlueprint):
    def __init__(self):
        super(Auth, self).__init__(import_name=__name__, name=BlueprintName.AUTH)

    def build_routes(self):
        def set_user_id_cookie(user_id):
            # todo implement me
            pass

        def is_logged_in():
            return False

        @self.route('/login', methods=['GET'])
        def login_get():
            # TODO check logged in
            if is_logged_in():
                return redirect(
                    BlueprintName.url_for(BlueprintName.SHARED, 'home_get')
                )

            return render_template('auth/login.html')

        @self.route('/login', methods=['POST'])
        def login_post():
            json_body = request.get_json()

            logged_in_user = User.login(
                email=json_body['email'],
                password=json_body['password']
            )

            set_user_id_cookie(logged_in_user.id)

        @self.route('/register', methods=['GET'])
        def register_get():
            # TODO check logged in
            if is_logged_in():
                return redirect(url_for('shared_pages.home'))

            return render_template('auth/register.html')

        @self.route('/register', methods=['POST'])
        def register_post():
            json_body = request.get_json()

            email = json_body['email']
            password = json_body['password']
            name = json_body['name']

            registered_user = User.register(
                email=email,
                password=password,
                name=name
            )

            set_user_id_cookie(registered_user.id)
