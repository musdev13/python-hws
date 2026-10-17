from datetime import datetime, date


class Stadium:
    DATE_FORMAT = "%Y-%m-%d"

    def __init__(self, name="", opening_date=None, country="", city="", capacity=0):
        self.name = name
        self.opening_date = opening_date if opening_date is not None else date(1900, 1, 1)
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Назва стадіону: ")
        raw_date = input(f"Дата відкриття (формат {self.DATE_FORMAT}): ")
        self.opening_date = datetime.strptime(raw_date, self.DATE_FORMAT).date()
        self.country = input("Країна: ")
        self.city = input("Місто: ")
        self.capacity = int(input("Місткість: "))

    def display(self):
        print(f"Назва: {self.name}")
        print(f"Дата відкриття: {self.opening_date.strftime(self.DATE_FORMAT)}")
        print(f"Країна: {self.country}")
        print(f"Місто: {self.city}")
        print(f"Місткість: {self.capacity}")

    def change_capacity(self, new_capacity):
        if new_capacity < 0:
            raise ValueError("Місткість не може бути від'ємною")
        self.capacity = new_capacity

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, new_capacity):
        self.change_capacity(new_capacity)

    def __str__(self):
        return (f"Stadium(name={self.name!r}, "
                f"opening_date={self.opening_date.strftime(self.DATE_FORMAT)}, "
                f"country={self.country!r}, city={self.city!r}, capacity={self.capacity})")

    def __eq__(self, other):
        if not isinstance(other, Stadium):
            return NotImplemented
        return (self.name == other.name and self.opening_date == other.opening_date
                and self.country == other.country and self.city == other.city
                and self.capacity == other.capacity)


if __name__ == "__main__":
    stadium1 = Stadium("Олімпійський", date(1923, 8, 12), "Україна", "Київ", 70050)
    stadium2 = Stadium("Олімпійський", date(1923, 8, 12), "Україна", "Київ", 70050)
    stadium3 = Stadium("Камп Ноу", date(1957, 9, 24), "Іспанія", "Барселона", 99354)

    print("Стадіон 1:")
    stadium1.display()
    print()
    print("str(stadium1):", stadium1)
    print("stadium1 == stadium2:", stadium1 == stadium2)
    print("stadium1 == stadium3:", stadium1 == stadium3)
    stadium1.change_capacity(65000)
    print("Після зміни місткості:", stadium1.get_capacity())
