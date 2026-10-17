from datetime import date


class Book:
    def __init__(self, title, author, year, pages):
        if not isinstance(pages, int) or pages < 0:
            raise ValueError("Кількість сторінок має бути невід'ємним цілим числом")
        if not isinstance(year, int) or not (21 < year <= date.today().year):
            raise ValueError(f"Рік видання має бути в діапазоні 22..{date.today().year}")
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' — {self.author} ({self.year}), {self.pages} стор."

    def __repr__(self):
        return (f"Book(title={self.title!r}, author={self.author!r}, "
                f"year={self.year}, pages={self.pages})")

    def __len__(self):
        return self.pages

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        if not isinstance(other, Book):
            return NotImplemented
        return self.pages < other.pages

    def __add__(self, other):
        if isinstance(other, Book):
            return self.pages + other.pages
        if isinstance(other, int):
            return self.pages + other
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, int):
            return other + self.pages
        return NotImplemented

    def __contains__(self, word):
        if not isinstance(word, str):
            return False
        return word.lower() in self.title.lower()

    def __bool__(self):
        return self.pages > 0


if __name__ == "__main__":
    b1 = Book("Кобзар", "Тарас Шевченко", 1840, 320)
    b2 = Book("Лісова пісня", "Леся Українка", 1911, 180)
    b3 = Book("Місто", "Валер'ян Підмогильний", 1928, 280)

    print("str:", str(b1))
    print("repr:", repr(b1))
    print("len(b1):", len(b1))
    print("b1 == b2:", b1 == b2)
    print("b1 < b3:", b1 < b3)
    print("b1 + b2:", b1 + b2)
    print("b1 + 10:", b1 + 10)
    print("'коб' in b1:", "коб" in b1)
    print("'Коб' in b1:", "Коб" in b1)
    print("'Місто' in b1:", "Місто" in b1)
    print("bool(b1):", bool(b1))

    empty = Book("Пуста", "Автор", 2020, 0)
    print("bool(empty):", bool(empty))

    books = [b1, b2, b3]
    print("sorted:", sorted(books))

    try:
        Book("Погана", "Автор", 1900, 100)
    except ValueError as e:
        print("Помилка року:", e)
    try:
        Book("Погана", "Автор", 2020, -5)
    except ValueError as e:
        print("Помилка сторінок:", e)
