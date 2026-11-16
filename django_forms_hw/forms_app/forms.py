from datetime import date

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(
        label="Логін",
        max_length=150,
        widget=forms.TextInput(attrs={"autocomplete": "username"}),
    )
    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )


class CalcForm(forms.Form):
    CHOICES = [
        ("min", "Мінімум із трьох"),
        ("max", "Максимум із трьох"),
        ("avg", "Середнє арифметичне із трьох"),
    ]

    a = forms.FloatField(label="Число 1")
    b = forms.FloatField(label="Число 2")
    c = forms.FloatField(label="Число 3")
    operation = forms.ChoiceField(
        label="Що знайти",
        choices=CHOICES,
        widget=forms.RadioSelect,
    )


class RegistrationForm(forms.Form):
    GENDERS = [
        ("M", "Чоловіча"),
        ("F", "Жіноча"),
        ("O", "Інша"),
    ]

    first_name = forms.CharField(label="Ім'я", max_length=100)
    last_name = forms.CharField(label="Прізвище", max_length=100)
    age = forms.IntegerField(label="Вік", min_value=1, max_value=120)
    email = forms.EmailField(label="Email")
    gender = forms.ChoiceField(label="Стать", choices=GENDERS, widget=forms.RadioSelect)
    address = forms.CharField(
        label="Адреса для доставки товару",
        widget=forms.Textarea(attrs={"rows": 3}),
    )
    newsletter = forms.BooleanField(
        label="Бажаєте підписатися на новини нашого інтернет-магазину?",
        required=False,
    )


class ProgrammerDayForm(forms.Form):
    year = forms.IntegerField(
        label="Рік",
        min_value=1,
        max_value=9999,
        widget=forms.NumberInput(attrs={"placeholder": "наприклад, 2021"}),
    )

    def clean_year(self):
        year = self.cleaned_data["year"]
        date(year, 1, 1)
        return year
