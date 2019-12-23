from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_title = models.CharField(max_length=200)
    movie_logo = models.CharField(max_length=500)
    movie_genres = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.movie_title + " - " + self.movie_genres