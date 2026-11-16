from datetime import date, timedelta

from django.contrib.auth import authenticate
from django.shortcuts import render

from .forms import CalcForm, LoginForm, ProgrammerDayForm, RegistrationForm

MONTHS_UK = [
    "січня", "лютого", "березня", "квітня", "травня", "червня",
    "липня", "серпня", "вересня", "жовтня", "листопада", "грудня",
]
WEEKDAYS_UK = [
    "понеділок", "вівторок", "середа", "четвер",
    "п'ятниця", "субота", "неділя",
]


def index(request):
    return render(request, "forms_app/index.html")


def task1(request):
    result = None
    is_error = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is None:
                result = "Неправильні параметри входу."
                is_error = True
            else:
                role = "Адміністратор" if user.is_staff else "Користувач"
                result = f"Вітаємо, {user.username}! Рівень доступу: {role}."
    else:
        form = LoginForm()
    return render(request, "forms_app/task1.html", {
        "form": form, "result": result, "is_error": is_error,
    })


def task2(request):
    result = None
    if request.method == "POST":
        form = CalcForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data["a"]
            b = form.cleaned_data["b"]
            c = form.cleaned_data["c"]
            op = form.cleaned_data["operation"]
            if op == "min":
                result = f"Мінімум із трьох: {min(a, b, c):g}"
            elif op == "max":
                result = f"Максимум із трьох: {max(a, b, c):g}"
            else:
                result = f"Середнє арифметичне із трьох: {(a + b + c) / 3:g}"
    else:
        form = CalcForm()
    return render(request, "forms_app/task2.html", {"form": form, "result": result})


def task3(request):
    result = None
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            result = {
                "Ім'я": data["first_name"],
                "Прізвище": data["last_name"],
                "Вік": data["age"],
                "Email": data["email"],
                "Стать": dict(RegistrationForm.GENDERS)[data["gender"]],
                "Адреса": data["address"],
                "Підписка на новини": "Так" if data["newsletter"] else "Ні",
            }
    else:
        form = RegistrationForm()
    return render(request, "forms_app/task3.html", {"form": form, "result": result})


def task4(request):
    result = None
    if request.method == "POST":
        form = ProgrammerDayForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data["year"]
            d = date(year, 1, 1) + timedelta(days=255)
            result = f"{d.day} {MONTHS_UK[d.month - 1]} ({WEEKDAYS_UK[d.weekday()]})"
    else:
        form = ProgrammerDayForm()
    return render(request, "forms_app/task4.html", {"form": form, "result": result})
