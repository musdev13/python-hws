class Device:
    def __init__(self, brand, model, power):
        if not isinstance(brand, str) or not brand.strip():
            raise ValueError("Бренд має бути непорожнім рядком")
        if not isinstance(model, str) or not model.strip():
            raise ValueError("Модель має бути непорожнім рядком")
        if not isinstance(power, int) or power <= 0:
            raise ValueError("Потужність має бути додатним цілим числом")
        self.brand = brand
        self.model = model
        self.power = power
        self.is_on = False

    def turn_on(self):
        if self.is_on:
            return f"{self.model} вже увімкнено"
        self.is_on = True
        return f"{self.model} увімкнено"

    def turn_off(self):
        if not self.is_on:
            return f"{self.model} вже вимкнено"
        self.is_on = False
        return f"{self.model} вимкнено"

    def __str__(self):
        state = "увімкнено" if self.is_on else "вимкнено"
        return f"{self.brand} {self.model} ({self.power} Вт, {state})"

    def __repr__(self):
        return (f"{self.__class__.__name__}(brand={self.brand!r}, "
                f"model={self.model!r}, power={self.power})")

    def __eq__(self, other):
        if not isinstance(other, Device):
            return NotImplemented
        return (self.brand, self.model, self.power) == (other.brand, other.model, other.power)


class CoffeeMachine(Device):
    def __init__(self, brand, model, power, water_ml=1000, beans_g=200):
        super().__init__(brand, model, power)
        if not isinstance(water_ml, int) or water_ml < 0:
            raise ValueError("Обсяг води має бути невід'ємним цілим числом")
        if not isinstance(beans_g, int) or beans_g < 0:
            raise ValueError("Кількість зерен має бути невід'ємним цілим числом")
        self.water_ml = water_ml
        self.beans_g = beans_g
        self.cups_made = 0

    def brew(self, size="small"):
        if not self.is_on:
            return "Спочатку увімкніть кавомашину"
        portions = {"small": (40, 8), "medium": (80, 15), "large": (120, 22)}
        if size not in portions:
            return f"Невідомий розмір: {size}"
        water, beans = portions[size]
        if self.water_ml < water:
            return "Недостатньо води"
        if self.beans_g < beans:
            return "Недостатньо зерен"
        self.water_ml -= water
        self.beans_g -= beans
        self.cups_made += 1
        return f"Готово: {size} кава ({water} мл, {beans} г зерен)"

    def clean(self):
        self.cups_made = 0
        return "Кавомашину очищено"

    def __str__(self):
        return (f"{super().__str__()} — вода: {self.water_ml} мл, "
                f"зерна: {self.beans_g} г, чашок: {self.cups_made}")


class Blender(Device):
    def __init__(self, brand, model, power, jar_ml=1500, max_speed=5):
        super().__init__(brand, model, power)
        if not isinstance(jar_ml, int) or jar_ml <= 0:
            raise ValueError("Обсяг чаші має бути додатним цілим числом")
        if not isinstance(max_speed, int) or max_speed <= 0:
            raise ValueError("Максимальна швидкість має бути додатним цілим числом")
        self.jar_ml = jar_ml
        self.max_speed = max_speed
        self.speed = 0

    def blend(self, seconds=10, speed=1):
        if not self.is_on:
            return "Спочатку увімкніть блендер"
        if not isinstance(seconds, int) or seconds <= 0:
            return "Час має бути додатним цілим числом"
        if not isinstance(speed, int) or not (1 <= speed <= self.max_speed):
            return f"Швидкість має бути в діапазоні 1..{self.max_speed}"
        self.speed = speed
        return f"Змішування {seconds} с на швидкості {speed}"

    def stop(self):
        self.speed = 0
        return "Блендер зупинено"

    def __str__(self):
        return (f"{super().__str__()} — чаша: {self.jar_ml} мл, "
                f"швидкість: {self.speed}/{self.max_speed}")


class MeatGrinder(Device):
    ATTACHMENTS = ("м'ясорубка", "терка", "сікач")

    def __init__(self, brand, model, power, attachment="м'ясорубка"):
        super().__init__(brand, model, power)
        if attachment not in self.ATTACHMENTS:
            raise ValueError(f"Невідома насадка: {attachment}")
        self.attachment = attachment
        self.processed_kg = 0.0

    def grind(self, kg):
        if not self.is_on:
            return "Спочатку увімкніть м'ясорубку"
        if not isinstance(kg, (int, float)) or kg <= 0:
            return "Маса має бути додатним числом"
        if self.attachment != "м'ясорубка":
            return f"Поточна насадка '{self.attachment}' не призначена для перемелювання"
        self.processed_kg += kg
        return f"Перемелено {kg} кг, всього: {self.processed_kg:.2f} кг"

    def change_attachment(self, attachment):
        if attachment not in self.ATTACHMENTS:
            return f"Невідома насадка: {attachment}"
        self.attachment = attachment
        return f"Встановлено насадку: {attachment}"

    def __str__(self):
        return (f"{super().__str__()} — насадка: {self.attachment}, "
                f"перемелено: {self.processed_kg:.2f} кг")


if __name__ == "__main__":
    cm = CoffeeMachine("DeLonghi", "ECAM", 1450)
    print(cm)
    print(cm.brew("medium"))
    print(cm.turn_on())
    print(cm.brew("medium"))
    print(cm.brew("large"))
    print(cm)
    print(cm.clean())

    bl = Blender("Bosch", "VitaPower", 800)
    print(bl)
    print(bl.blend(15, 3))
    print(bl.turn_on())
    print(bl.blend(15, 3))
    print(bl.blend(15, 10))
    print(bl)
    print(bl.stop())

    mg = MeatGrinder("Philips", "HR2727", 500)
    print(mg)
    print(mg.grind(2))
    print(mg.turn_on())
    print(mg.grind(2))
    print(mg.change_attachment("терка"))
    print(mg.grind(1))
    print(mg.change_attachment("м'ясорубка"))
    print(mg.grind(1.5))
    print(mg)

    print("Рівність:", CoffeeMachine("A", "B", 100) == CoffeeMachine("A", "B", 100))

    try:
        CoffeeMachine("", "X", 100)
    except ValueError as e:
        print("Помилка:", e)
    try:
        Blender("X", "Y", -5)
    except ValueError as e:
        print("Помилка:", e)
    try:
        MeatGrinder("X", "Y", 100, "невідомо")
    except ValueError as e:
        print("Помилка:", e)
