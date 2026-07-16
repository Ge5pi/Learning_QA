import pytest
from app.auth import User

@pytest.mark.parametrize(
    "username, password",
    [
        ("gespi", "gespi"),
        ("123123", "123123"),
        ("abcde",  "qwerty")
    ]
)
def test_register_user(empty_auth_service, username, password):
    empty_auth_service.register(username, password)
    assert isinstance(empty_auth_service.users[username], User)
    assert empty_auth_service.users[username].password_hash != password
    assert empty_auth_service.users[username].username == username

def test_login_user(auth_service):
    user = auth_service.login("gespi", "gespi")
    assert user.username == "gespi"

def test_login_user_with_wrong_password(auth_service):
    with pytest.raises(ValueError, match="Invalid password"):
        auth_service.login("gespi", "123123")

def test_login_user_with_wrong_username(auth_service):
    with pytest.raises(ValueError, match="User not found"):
        auth_service.login("123123", "gespi")

def test_register_existing_user(auth_service):
    with pytest.raises(ValueError, match="User already exists"):
        auth_service.register(username="gespi", password="gespi")
