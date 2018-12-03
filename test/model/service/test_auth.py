from model.service.auth_service import AuthService
from test.base_classes.base_test import BaseTest


class TestAuth(BaseTest):

    def setUp(self):
        super(TestAuth, self).setUp()
        self.auth_service = AuthService()
        self.password = 'test_password'

    def test_password_verifies(self):
        assert self.auth_service.verify_password(
            plaintext_password=self.password,
            password_hash=self.auth_service.hash_password(self.password)
        )

    def test_incorrect_password_fails(self):
        assert not self.auth_service.verify_password(
            plaintext_password=self.password,
            password_hash=self.auth_service.hash_password('wrong_password')
        )
