class Car:
    def __init__(self, model="", year=0, manufacturer="", engine_volume=0.0, color="", price=0.0):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_volume = engine_volume
        self.color = color
        self.price = price

    def input_data(self):
        self.model = input("Модель: ")
        self.year = int(input("Рік випуску: "))
        self.manufacturer = input("Виробник: ")
        self.engine_volume = float(input("Об'єм двигуна (л): "))
        self.color = input("Колір: ")
        self.price = float(input("Ціна: "))

    def display(self):
        print(f"Модель: {self.model}")
        print(f"Рік випуску: {self.year}")
        print(f"Виробник: {self.manufacturer}")
        print(f"Об'єм двигуна: {self.engine_volume} л")
        print(f"Колір: {self.color}")
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
        return (f"Car(model={self.model!r}, year={self.year}, manufacturer={self.manufacturer!r}, "
                f"engine_volume={self.engine_volume}, color={self.color!r}, price={self.price})")

    def __eq__(self, other):
        if not isinstance(other, Car):
            return NotImplemented
        return (self.model == other.model and self.year == other.year
                and self.manufacturer == other.manufacturer
                and self.engine_volume == other.engine_volume
                and self.color == other.color and self.price == other.price)


if __name__ == "__main__":
    car1 = Car("Camry", 2020, "Toyota", 2.5, "black", 25000.0)
    car2 = Car("Camry", 2020, "Toyota", 2.5, "black", 25000.0)
    car3 = Car("Accord", 2019, "Honda", 2.0, "white", 22000.0)

    print("Автомобіль 1:")
    car1.display()
    print()
    print("str(car1):", car1)
    print("car1 == car2:", car1 == car2)
    print("car1 == car3:", car1 == car3)
    car1.change_price(24000.0)
    print("Після зміни ціни:", car1.get_price())
