from passlib.handlers.pbkdf2 import pbkdf2_sha256


class AuthService:
    def __init__(
            self,
            hash_rounds: int = 200000,
            salt_size: int = 16
    ):
        self.hash_rounds = hash_rounds
        self.salt_size = salt_size

    def hash_password(self, plaintext_password: str) -> str:
        return pbkdf2_sha256.using(
            rounds=self.hash_rounds,
            salt_size=self.salt_size
        ).hash(
            plaintext_password
        )

    def verify_password(self, plaintext_password: str, password_hash: str) -> bool:
        return pbkdf2_sha256.verify(plaintext_password, password_hash)
