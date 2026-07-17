import pytest


@pytest.mark.parametrize(
    "amount",
    [
        100,
        200,
        300
     ]
)
def test_successful_order_creation(order_service, amount):
    result = order_service.checkout(amount)
    assert result == "Order created"
    order_service.payment.pay.assert_called_once_with(amount)

@pytest.mark.parametrize(
    "amount",
    [0,
     -100,
     -200]
)
def test_failed_checkout_creation(order_service, amount):
    with pytest.raises(ValueError, match="Total must be positive"):
        order_service.checkout(amount)
    order_service.payment.pay.assert_not_called()

def test_failed_payment_creation(order_service_false):
    result = order_service_false.checkout(100)
    assert result == "Payment failed"
    order_service_false.payment.pay.assert_called_once_with(100)