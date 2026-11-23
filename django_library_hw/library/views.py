from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Exists, OuterRef
from django.views.generic import DetailView, ListView

from .models import Book, Loan, Reader


def books_with_availability():
    return Book.objects.annotate(
        has_active_loan=Exists(
            Loan.objects.filter(book=OuterRef('pk'), returned_at__isnull=True)
        )
    )


class BookListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'
    permission_required = 'library.view_book'

    def get_queryset(self):
        queryset = books_with_availability()
        if self.request.GET.get('availability') == 'available':
            queryset = queryset.filter(has_active_loan=False)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['availability'] = self.request.GET.get('availability', 'all')
        return context


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'
    permission_required = 'library.view_book'

    def get_queryset(self):
        return books_with_availability()


class ReaderListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Reader
    template_name = 'library/reader_list.html'
    context_object_name = 'readers'
    permission_required = 'library.view_reader'


class ReaderDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Reader
    template_name = 'library/reader_detail.html'
    context_object_name = 'reader'
    permission_required = ('library.view_reader', 'library.view_loan')

    def get_queryset(self):
        return Reader.objects.prefetch_related('loans__book')
