import json




class LoggingMixin:
    def log(self, message):
        print(f"[LOG] {message}")

class JsonMixin:
    def to_json(self):
        return json.dumps(
            {"name": self.name, "price": self.price},
            ensure_ascii=False
        )

class DiscountMixin:
    def apply_discount(self, percent):
        if not 0 <= percent <= 100:
            raise ValueError("Відсоток знижки має бути від 0 до 100")

        self.price = round(self.price * (1 - percent / 100), 2)
        self.log(f"Застосовано знижку {percent}%. Нова ціна: {self.price} грн")
        return self.price




class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} грн"

class ProductManager(Product, LoggingMixin, JsonMixin, DiscountMixin):
    pass




product = ProductManager("Ноутбук", 1000)

print(product.to_json())
product.apply_discount(15)
print(product.price)
print(product.to_json())


print(ProductManager.mro())
