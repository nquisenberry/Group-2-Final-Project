from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_year = models.IntegerField()
    runtime = models.IntegerField()
    genres = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    favorite_movies = models.ManyToManyField(
        Movie,
        related_name="favorites",
        blank=True
    )

    disliked_movies = models.ManyToManyField(
        Movie,
        related_name="dislikes",
        blank=True
    )

    def __str__(self):
        return self.user.username
