from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    BookListView, BookDetailView, BookCreateView,
    BookUpdateView, BookDeleteView,
    AuthorViewSet, BookViewSet
)

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', include(router.urls)),
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update', BookUpdateView.as_view(), name='book-update'),
    path('books/delete', BookDeleteView.as_view(), name='book-delete'),
]

