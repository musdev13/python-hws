class Product:
    def __init__(self, id, title, image, price, rating):
        self.id = id
        self.title = title
        self.image = image
        self.price = price
        self.rating = rating

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "image": self.image,
            "price": self.price,
            "rating": self.rating
        }
