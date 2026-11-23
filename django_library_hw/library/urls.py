from django.urls import path

from .views import BookDetailView, BookListView, ReaderDetailView, ReaderListView

urlpatterns = [
    path('', BookListView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('readers/', ReaderListView.as_view(), name='readers'),
    path('readers/<int:pk>/', ReaderDetailView.as_view(), name='reader_detail'),
]
