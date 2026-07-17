from app.payment import PaymentService


class OrderService:

    def __init__(self):
        self.payment = PaymentService()

    def checkout(self, total: float):

        if total <= 0:
            raise ValueError("Total must be positive")

        if self.payment.pay(total):
            return "Order created"

        return "Payment failed"