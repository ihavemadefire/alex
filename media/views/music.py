from django.views.generic import ListView, DetailView
from ..models import Music


class MusicListView(ListView):
    model = Music
    template_name = "music_list.html"
    context_object_name = "music_list"


class MusicDetailView(DetailView):
    model = Music
    template_name = "music_detail.html"
    context_object_name = "music"
