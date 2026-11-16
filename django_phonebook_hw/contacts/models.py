from django.db import models


class Contact(models.Model):
    first_name = models.CharField("Ім'я", max_length=100)
    last_name = models.CharField("Прізвище", max_length=100)
    email = models.EmailField("Email")
    phone = models.CharField("Контактний телефон", max_length=32)
    notes = models.TextField("Примітки", blank=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Контакт"
        verbose_name_plural = "Контакти"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
