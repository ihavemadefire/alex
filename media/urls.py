from django.urls import path
from .views import (
    BookListView, BookDetailView,
    MovieListView, MovieDetailView,
    MusicListView, MusicDetailView,
    BookCreateView, BookCreateFromISBNView
)

app_name = 'media'

urlpatterns = [
    path('books/', BookListView.as_view(), name='books'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/add/', BookCreateView.as_view(), name='book-add'),
    path('books/add-isbn/', BookCreateFromISBNView.as_view(), name='book-add-isbn'),

    path('movies/', MovieListView.as_view(), name='movies'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),

    path('music/', MusicListView.as_view(), name='music'),
    path('music/<int:pk>/', MusicDetailView.as_view(), name='music-detail'),
]
