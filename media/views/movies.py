from django.views.generic import DetailView, ListView
from ..models import Movie


class MovieDetailView(DetailView):
    model = Movie
    template_name = "movie.html"
    context_object_name = "movie"


class MovieListView(ListView):
    model = Movie
    template_name = "movies.html"
    context_object_name = "movies"
