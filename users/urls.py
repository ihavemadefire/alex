from django.urls import path
from .views import (
    BookListView, BookDetailView,
    MovieListView, MovieDetailView,
    MusicListView, MusicDetailView
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),

    path('music/', MusicListView.as_view(), name='music-list'),
    path('music/<int:pk>/', MusicDetailView.as_view(), name='music-detail'),
]
