class PaymentService:

    def pay(self, amount: float) -> bool:
        print(f"Paid {amount}")
        return True