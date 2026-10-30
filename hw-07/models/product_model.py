from product import Product

class ProductModel:
    def __init__(self):
        self.products = [
            Product(1, "Ноутбук", "https://via.placeholder.com/150", 25000, 4.5),
            Product(2, "Смартфон", "https://via.placeholder.com/150", 15000, 4.8),
            Product(3, "Навушники", "https://via.placeholder.com/150", 3000, 4.2),
        ]

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.id == product_id:
                return product
        return None

    def create_product(self, product):
        self.products.append(product)
        return product
