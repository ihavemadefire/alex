from django.db import models
from django.conf import settings

class BaseMedia(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    notes = models.TextField(blank=True)
    added_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Book(BaseMedia):
    isbn = models.CharField(max_length=20, blank=True)
    publisher = models.CharField(max_length=255, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    fiction_non_fiction = models.CharField(max_length=50, choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction')], blank=True)

class Movie(BaseMedia):
    director = models.CharField(max_length=255, blank=True)
    runtime_minutes = models.IntegerField(blank=True, null=True)
    format = models.CharField(max_length=50, choices=[('DVD', 'DVD'), ('Blu-ray', 'Blu-ray'), ('Digital', 'Digital')], blank=True)

class Music(BaseMedia):
    artist = models.CharField(max_length=255, blank=True)
    format = models.CharField(max_length=50, choices=[('CD', 'CD'), ('Vinyl', 'Vinyl'), ('Digital', 'Digital')], blank=True)
    genre = models.CharField(max_length=100, blank=True)

class Game(BaseMedia):
    platform = models.CharField(max_length=100, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    publisher = models.CharField(max_length=255, blank=True)
    release_date = models.DateField(blank=True, null=True)