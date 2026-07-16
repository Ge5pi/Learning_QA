class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price


class ProductService:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)

    def get_product(self, name: str):
        for product in self.products:
            if product.name == name:
                return product
        raise ValueError("Product not found")

    def apply_discount(self, name: str, percent: int):
        product = self.get_product(name)
        product.price *= (100 - percent) / 100