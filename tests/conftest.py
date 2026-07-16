from app.cart import Cart
import pytest
from app.products import Product, ProductService
from app.auth import AuthService, User

@pytest.fixture
def cart():
    return Cart()

@pytest.fixture
def empty_product_service():
    product_service = ProductService()
    return product_service

@pytest.fixture
def product():
    return Product("Bread", 200)

@pytest.fixture
def product_service(product):
    product_service = ProductService()
    product_service.add_product(product)
    return product_service

@pytest.fixture
def empty_auth_service():
    auth = AuthService()
    return auth

@pytest.fixture
def auth_service():
    auth = AuthService()
    auth.register("gespi", "gespi")
    return auth
