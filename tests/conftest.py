from app.cart import Cart
import pytest
from app.products import Product, ProductService

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
