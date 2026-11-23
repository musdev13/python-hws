from django.db import models
from django.db.models import Q


class Book(models.Model):
    title = models.CharField('назва книги', max_length=200)
    author = models.CharField('автор', max_length=200)
    publication_year = models.PositiveSmallIntegerField('рік видання')
    genre = models.CharField('жанр', max_length=100)
    publisher = models.CharField('видавництво', max_length=200)

    class Meta:
        ordering = ['title', 'author']
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return f'{self.title} — {self.author}'


class Reader(models.Model):
    first_name = models.CharField('ім’я', max_length=100)
    last_name = models.CharField('прізвище', max_length=100)
    phone = models.CharField('контактний телефон', max_length=30)
    email = models.EmailField('email', unique=True)
    joined_at = models.DateField('дата запису', auto_now_add=True)

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'читач'
        verbose_name_plural = 'читачі'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Loan(models.Model):
    reader = models.ForeignKey(
        Reader,
        on_delete=models.CASCADE,
        related_name='loans',
        verbose_name='читач',
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        related_name='loans',
        verbose_name='книга',
    )
    borrowed_at = models.DateField('дата видачі', auto_now_add=True)
    returned_at = models.DateField('дата повернення', null=True, blank=True)

    class Meta:
        ordering = ['-borrowed_at']
        verbose_name = 'видача книги'
        verbose_name_plural = 'видачі книг'
        constraints = [
            models.UniqueConstraint(
                fields=['book'],
                condition=Q(returned_at__isnull=True),
                name='one_active_loan_per_book',
            ),
        ]

    def __str__(self):
        return f'{self.book} — {self.reader}'
