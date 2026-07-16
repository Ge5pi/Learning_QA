from app.cart import Cart
import pytest

@pytest.fixture
def cart():
    return Cart()