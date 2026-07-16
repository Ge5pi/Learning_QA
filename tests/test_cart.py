import pytest

def test_cart_creation(cart):
    assert cart.total_items() == 0

def test_cart_add(cart):
    cart.add("Bread")
    assert cart.total_items() == 1

def test_add_multiple(cart):
    cart.add("Bread")
    cart.add("Cheese")
    assert cart.total_items() == 2

def test_cart_remove(cart):
    cart.add("Bread")
    cart.remove("Bread")
    assert cart.total_items() == 0

def test_remove_exception(cart):
    with pytest.raises(ValueError, match="Product not found"):
        cart.remove("Bread")

def test_clear(cart):
    cart.add("Bread")
    cart.add("Cheese")
    cart.clear()
    assert cart.total_items() == 0

def test_length(cart):
    cart.add("Bread")
    cart.add("Cheese")
    assert cart.total_items() == 2