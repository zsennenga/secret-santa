from flask import request, render_template, flash
from flask_login import current_user, login_user
from werkzeug.utils import redirect

from app.blueprint.base_blueprint import BaseBlueprint
from app.forms import SignupForm, LoginForm
from constant.blueprint_name import BlueprintName
from model.table.user import User


class Auth(BaseBlueprint):
    def __init__(self):
        super(Auth, self).__init__(import_name=__name__, name=BlueprintName.AUTH.value, url_prefix='/auth')

    def build_routes(self):
        @self.route('/login', methods=['GET'])
        def login_get():
            if current_user.is_authenticated:
                return redirect(
                    BlueprintName.SHARED.url_for('home_get')
                )

            return render_template('auth/login.html', form=LoginForm())

        @self.route('/login', methods=['POST'])
        def login_post():
            for field in ['email', 'password']:
                if field not in request.form:
                    flash(f'{field} is missing from the request', 'error')
                    return BlueprintName.AUTH.redirect('login_get')

            email = request.form['email']
            password = request.form['password']

            try:
                logged_in_user = User.login(
                    email=email,
                    plaintext_password=password
                )
                login_user(logged_in_user)
            except Exception as e:
                flash(str(e), 'error')
                return BlueprintName.AUTH.redirect('login_get')

            return BlueprintName.EXCHANGES.redirect('exchanges_get')

        @self.route('/register', methods=['GET'])
        def register_get():
            if current_user.is_authenticated:
                return BlueprintName.SHARED.redirect('home_get')

            return render_template('auth/register.html', form=SignupForm())

        @self.route('/register', methods=['POST'])
        def register_post():
            for field in ['email', 'password', 'name']:
                if field not in request.form:
                    flash(f'{field} is missing from the request', 'error')
                    return BlueprintName.AUTH.redirect('register_get')

            try:
                registered_user = User.register(
                    email=request.form['email'],
                    plaintext_password=request.form['password'],
                    name=request.form['name']
                )

                login_user(registered_user)
            except Exception as e:
                flash(str(e), 'error')
                return BlueprintName.AUTH.redirect('register_get')

            return BlueprintName.EXCHANGES.redirect('exchanges_get')
