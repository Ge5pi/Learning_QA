import pytest

def test_product_addition(empty_product_service, product):
    empty_product_service.add_product(product)
    result = empty_product_service.get_product(product.name)
    assert result.price == product.price
    assert result.name == product.name

def test_get_product(product_service, product):
    result = product_service.get_product(product.name)
    assert result.name == product.name
    assert result.price == product.price

def test_get_product_with_empty_list(empty_product_service, product):
    with pytest.raises(ValueError, match="Product not found"):
        empty_product_service.get_product(product.name)

@pytest.mark.parametrize(
    "discount, expected",
    [
        (0, 200),
        (10, 180),
        (50, 100),
    ],
    ids=[
        "no_discount",
        "ten_percent",
        "half_price"
    ]
)
def test_apply_discount(product_service, product, discount, expected):
    product_service.apply_discount(product.name, discount)
    assert product.price == pytest.approx(expected)

