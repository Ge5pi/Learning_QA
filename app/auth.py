import hashlib


class User:
    def __init__(self, username: str, password_hash: str):
        self.username = username
        self.password_hash = password_hash


class AuthService:
    def __init__(self):
        self.users = {}

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username: str, password: str):
        if username in self.users:
            raise ValueError("User already exists")

        self.users[username] = User(
            username,
            self._hash_password(password)
        )

    def login(self, username: str, password: str):
        if username not in self.users:
            raise ValueError("User not found")

        user = self.users[username]

        if user.password_hash != self._hash_password(password):
            raise ValueError("Invalid password")

        return user