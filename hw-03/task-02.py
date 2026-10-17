class Book:
    def __init__(self, title="", year=0, publisher="", genre="", author="", price=0.0):
        self.title = title
        self.year = year
        self.publisher = publisher
        self.genre = genre
        self.author = author
        self.price = price

    def input_data(self):
        self.title = input("Назва книги: ")
        self.year = int(input("Рік видання: "))
        self.publisher = input("Видавець: ")
        self.genre = input("Жанр: ")
        self.author = input("Автор: ")
        self.price = float(input("Ціна: "))

    def display(self):
        print(f"Назва: {self.title}")
        print(f"Рік видання: {self.year}")
        print(f"Видавець: {self.publisher}")
        print(f"Жанр: {self.genre}")
        print(f"Автор: {self.author}")
        print(f"Ціна: {self.price}")

    def change_price(self, new_price):
        if new_price < 0:
            raise ValueError("Ціна не може бути від'ємною")
        self.price = new_price

    def get_price(self):
        return self.price

    def set_price(self, new_price):
        self.change_price(new_price)

    def __str__(self):
        return (f"Book(title={self.title!r}, year={self.year}, publisher={self.publisher!r}, "
                f"genre={self.genre!r}, author={self.author!r}, price={self.price})")

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return (self.title == other.title and self.year == other.year
                and self.publisher == other.publisher and self.genre == other.genre
                and self.author == other.author and self.price == other.price)


if __name__ == "__main__":
    book1 = Book("Кобзар", 1840, "Просвіта", "поезія", "Тарас Шевченко", 350.0)
    book2 = Book("Кобзар", 1840, "Просвіта", "поезія", "Тарас Шевченко", 350.0)
    book3 = Book("Лісова пісня", 1911, "Дніпро", "драма", "Леся Українка", 280.0)

    print("Книга 1:")
    book1.display()
    print()
    print("str(book1):", book1)
    print("book1 == book2:", book1 == book2)
    print("book1 == book3:", book1 == book3)
    book1.change_price(320.0)
    print("Після зміни ціни:", book1.get_price())
