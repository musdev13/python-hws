class Ship:
    def __init__(self, name, displacement, crew, max_speed):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Назва має бути непорожнім рядком")
        if not isinstance(displacement, (int, float)) or displacement <= 0:
            raise ValueError("Водотоннажність має бути додатним числом")
        if not isinstance(crew, int) or crew <= 0:
            raise ValueError("Екіпаж має бути додатним цілим числом")
        if not isinstance(max_speed, (int, float)) or max_speed <= 0:
            raise ValueError("Максимальна швидкість має бути додатним числом")
        self.name = name
        self.displacement = displacement
        self.crew = crew
        self.max_speed = max_speed
        self.speed = 0.0

    def move(self, speed):
        if not isinstance(speed, (int, float)) or speed < 0:
            return "Швидкість має бути невід'ємним числом"
        if speed > self.max_speed:
            return f"Максимальна швидкість — {self.max_speed} вузлів"
        self.speed = float(speed)
        if speed == 0:
            return f"{self.name} зупинено"
        return f"{self.name} рухається зі швидкістю {speed} вузлів"

    def stop(self):
        self.speed = 0.0
        return f"{self.name} зупинено"

    def __str__(self):
        return (f"{self.name} — {self.displacement} т, екіпаж {self.crew} ос., "
                f"швидкість {self.speed}/{self.max_speed} вузлів")

    def __repr__(self):
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"displacement={self.displacement}, crew={self.crew}, "
                f"max_speed={self.max_speed})")

    def __eq__(self, other):
        if not isinstance(other, Ship):
            return NotImplemented
        return (self.name, self.displacement, self.crew, self.max_speed) == (
            other.name, other.displacement, other.crew, other.max_speed)


class Frigate(Ship):
    def __init__(self, name, displacement, crew, max_speed, missiles=8):
        super().__init__(name, displacement, crew, max_speed)
        if not isinstance(missiles, int) or missiles < 0:
            raise ValueError("Кількість ракет має бути невід'ємним цілим числом")
        self.missiles = missiles

    def launch_missile(self):
        if self.missiles <= 0:
            return "Ракет немає"
        self.missiles -= 1
        return f"Запущено ракету, залишилось: {self.missiles}"

    def reload(self, count):
        if not isinstance(count, int) or count <= 0:
            return "Кількість має бути додатним цілим числом"
        self.missiles += count
        return f"Завантажено {count} ракет, всього: {self.missiles}"

    def __str__(self):
        return f"{super().__str__()} — фрегат, ракет: {self.missiles}"


class Destroyer(Ship):
    def __init__(self, name, displacement, crew, max_speed, torpedoes=10):
        super().__init__(name, displacement, crew, max_speed)
        if not isinstance(torpedoes, int) or torpedoes < 0:
            raise ValueError("Кількість торпед має бути невід'ємним цілим числом")
        self.torpedoes = torpedoes

    def fire_torpedo(self):
        if self.torpedoes <= 0:
            return "Торпед немає"
        self.torpedoes -= 1
        return f"Запущено торпеду, залишилось: {self.torpedoes}"

    def reload(self, count):
        if not isinstance(count, int) or count <= 0:
            return "Кількість має бути додатним цілим числом"
        self.torpedoes += count
        return f"Завантажено {count} торпед, всього: {self.torpedoes}"

    def __str__(self):
        return f"{super().__str__()} — есмінець, торпед: {self.torpedoes}"


class Cruiser(Ship):
    def __init__(self, name, displacement, crew, max_speed, aircraft=2):
        super().__init__(name, displacement, crew, max_speed)
        if not isinstance(aircraft, int) or aircraft < 0:
            raise ValueError("Кількість літаків має бути невід'ємним цілим числом")
        self.aircraft = aircraft
        self.airborne = 0

    def launch_aircraft(self):
        if self.aircraft <= 0:
            return "Немає літаків на борту"
        self.aircraft -= 1
        self.airborne += 1
        return f"Літак злетів, на борту: {self.aircraft}, у повітрі: {self.airborne}"

    def land_aircraft(self):
        if self.airborne <= 0:
            return "Немає літаків у повітрі"
        self.airborne -= 1
        self.aircraft += 1
        return f"Літак сів, на борту: {self.aircraft}, у повітрі: {self.airborne}"

    def __str__(self):
        return (f"{super().__str__()} — крейсер, літаків на борту: {self.aircraft}, "
                f"у повітрі: {self.airborne}")


if __name__ == "__main__":
    f = Frigate("Гетьман Сагайдачний", 3200, 180, 32)
    print(f)
    print(f.move(20))
    print(f.launch_missile())
    print(f.launch_missile())
    print(f.reload(5))
    print(f)
    print(f.stop())

    d = Destroyer("Безстрашний", 4500, 250, 30)
    print(d)
    print(d.move(40))
    print(d.fire_torpedo())
    print(d.reload(3))
    print(d)

    c = Cruiser("Україна", 12000, 500, 32)
    print(c)
    print(c.launch_aircraft())
    print(c.launch_aircraft())
    print(c.launch_aircraft())
    print(c.land_aircraft())
    print(c)

    print("Рівність:", Frigate("A", 100, 10, 20) == Frigate("A", 100, 10, 20))
    print("Різна поведінка підкласів:")
    for s in (f, d, c):
        print(" ", s)

    try:
        Ship("", 100, 10, 20)
    except ValueError as e:
        print("Помилка:", e)
    try:
        Destroyer("X", -1, 10, 20)
    except ValueError as e:
        print("Помилка:", e)
