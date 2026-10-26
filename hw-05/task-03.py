class Money:
    def __init__(self, whole=0, cents=0, currency="грн"):
        if not isinstance(currency, str) or not currency.strip():
            raise ValueError("Валюта має бути непорожнім рядком")
        self.currency = currency
        self._normalize(whole, cents)

    def _normalize(self, whole, cents):
        if not isinstance(whole, int):
            raise ValueError("Ціла частина має бути цілим числом")
        if not isinstance(cents, int):
            raise ValueError("Копійки мають бути цілим числом")
        total = whole * 100 + cents
        self.whole = total // 100
        self.cents = total % 100

    def set(self, whole, cents):
        self._normalize(whole, cents)
        return self

    def get(self):
        return self.whole, self.cents

    def display(self):
        return f"{self.whole}.{self.cents:02d} {self.currency}"

    def total_cents(self):
        return self.whole * 100 + self.cents

    def __str__(self):
        return self.display()

    def __repr__(self):
        return f"{self.__class__.__name__}(whole={self.whole}, cents={self.cents}, currency={self.currency!r})"

    def _check_currency(self, other):
        if not isinstance(other, Money):
            return False
        if self.currency != other.currency:
            raise ValueError(f"Різні валюти: {self.currency} та {other.currency}")
        return True

    def __eq__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return self.currency == other.currency and self.total_cents() == other.total_cents()

    def __lt__(self, other):
        if not self._check_currency(other):
            return NotImplemented
        return self.total_cents() < other.total_cents()

    def __le__(self, other):
        if not self._check_currency(other):
            return NotImplemented
        return self.total_cents() <= other.total_cents()

    def __add__(self, other):
        if not self._check_currency(other):
            return NotImplemented
        return Money(0, self.total_cents() + other.total_cents(), self.currency)

    def __sub__(self, other):
        if not self._check_currency(other):
            return NotImplemented
        diff = self.total_cents() - other.total_cents()
        if diff < 0:
            raise ValueError("Результат від'ємний")
        return Money(0, diff, self.currency)


class Product(Money):
    def __init__(self, name, whole=0, cents=0, currency="грн"):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Назва продукту має бути непорожнім рядком")
        super().__init__(whole, cents, currency)
        self.name = name

    def reduce_price(self, amount):
        if isinstance(amount, Money):
            if amount.currency != self.currency:
                raise ValueError(f"Різні валюти: {self.currency} та {amount.currency}")
            diff = self.total_cents() - amount.total_cents()
        elif isinstance(amount, (int, float)):
            diff = self.total_cents() - int(round(amount * 100))
        else:
            raise ValueError("Сума зниження має бути Money або числом")
        if diff < 0:
            raise ValueError("Ціна не може стати від'ємною")
        self._normalize(0, diff)
        return self

    def __str__(self):
        return f"{self.name}: {self.display()}"

    def __repr__(self):
        return (f"Product(name={self.name!r}, whole={self.whole}, "
                f"cents={self.cents}, currency={self.currency!r})")


if __name__ == "__main__":
    m1 = Money(10, 50)
    m2 = Money(3, 75, "грн")
    print("m1:", m1)
    print("m2:", m2)
    print("m1 + m2:", m1 + m2)
    print("m1 - m2:", m1 - m2)
    print("m1 > m2:", m1 > m2)
    print("m1 == m2:", m1 == m2)

    print("нормалізація 5.150:", Money(5, 150))
    print("set:", Money().set(2, 5))

    p = Product("Кава", 12, 99)
    print("товар:", p)
    p.reduce_price(2.50)
    print("після знижки 2.50:", p)
    p.reduce_price(Money(0, 49))
    print("після знижки 0.49:", p)

    try:
        Money(1, 0, "грн") + Money(1, 0, "usd")
    except ValueError as e:
        print("Помилка валюти:", e)
    try:
        Product("X", 1, 0).reduce_price(5)
    except ValueError as e:
        print("Помилка знижки:", e)
    try:
        Product("", 1, 0)
    except ValueError as e:
        print("Помилка назви:", e)
