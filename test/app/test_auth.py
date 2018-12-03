from flask import Response

from constant.blueprint_name import BlueprintName
from model.service.auth_service import AuthService
from model.table.user import User
from test.base_classes.base_test import BaseTest


class TestAuth(BaseTest):

    def setUp(self):
        super(TestAuth, self).setUp()
        self.email = 'test_email'
        self.password = 'test_password'
        self.name = 'test_name'

    def _register_post(self, email=None, password=None, name=None) -> Response:
        return self.client.post(
            BlueprintName.AUTH.url_for('register_post'),
            data={
                'email': email or self.email,
                'password': password or self.password,
                'name': name or self.name
            }
        )

    def _login_user(self, email=None, password=None) -> Response:
        return self.client.post(
            BlueprintName.AUTH.url_for('login_post'),
            data={
                'email': email or self.email,
                'password': password or self.password
            }
        )

    def _verify_user(self, user_id):
        user = User.get_by_id(user_id)

        assert user.id == int(user_id)
        assert user.email == self.email
        assert user.name == self.name

        assert AuthService().verify_password(plaintext_password=self.password, password_hash=user.password)

    def test_register_creates_user(self):
        user_id = self._register_post().get_data().decode()

        self._verify_user(user_id)

        return user_id

    def test_login_user(self):
        user = User.register(
            email=self.email,
            name=self.name,
            plaintext_password=self.password
        )

        response = self._login_user().get_data().decode()

        assert int(response) == user.id

        self._verify_user(user.id)

    def test_login_nonexistent_user(self):
        response = self._login_user()

        assert response.status_code == 401

    def test_login_wrong_password(self):
        self._register_post()
        response = self._login_user(password="wrong_password")

        assert response.status_code == 401

    def test_register_with_existing_email(self):
        response = self._register_post()

        assert response.status_code == 200

        response = self._register_post()

        assert response.status_code == 400

    def test_missing_required_field_login(self):
        for field in ['email', 'password']:
            body = {
                'email': self.email,
                'password': self.password,
            }
            del body[field]

            response = self.client.post(
                BlueprintName.AUTH.url_for('login_post'),
                data=body
            )

            assert response.status_code == 400
            assert field in response.get_data().decode()

    def test_missing_required_field_register(self):
        for field in ['email', 'password', 'name']:
            body = {
                'email': self.email,
                'password': self.password,
                'name': self.name,
            }
            del body[field]

            response = self.client.post(
                BlueprintName.AUTH.url_for('register_post'),
                data=body
            )

            assert response.status_code == 400
            assert field in response.get_data().decode()
