from django.contrib import admin

from .models import Book, Loan, Reader


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'genre', 'publisher')
    search_fields = ('title', 'author', 'publisher')
    list_filter = ('genre', 'publication_year')


class LoanInline(admin.TabularInline):
    model = Loan
    extra = 1


@admin.register(Reader)
class ReaderAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone', 'email', 'joined_at')
    search_fields = ('first_name', 'last_name', 'email')
    inlines = (LoanInline,)


@admin.register(Loan)
class LoanAdmin(admin.ModelAdmin):
    list_display = ('book', 'reader', 'borrowed_at', 'returned_at')
    list_filter = ('borrowed_at', 'returned_at')
