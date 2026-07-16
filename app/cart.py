class Cart:
    def __init__(self):
        self.items = []

    def add(self, product: str):
        self.items.append(product)

    def remove(self, product: str):
        if product not in self.items:
            raise ValueError("Product not found")
        self.items.remove(product)

    def total_items(self):
        return len(self.items)

    def clear(self):
        self.items.clear()