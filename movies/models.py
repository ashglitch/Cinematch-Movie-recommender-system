
from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    GENRE_CHOICES = [
        ("Action", "Action"),
        ("Comedy", "Comedy"),
        ("Drama", "Drama"),
        ("Sci-Fi", "Sci-Fi"),
        ("Romance", "Romance"),
        ("Horror", "Horror"),
        ("Thriller", "Thriller"),
        ("Animation", "Animation"),
        ("Adventure", "Adventure"),
        ("Fantasy", "Fantasy"),
    ]

    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    year = models.PositiveIntegerField()
    description = models.TextField(default="No description available.")
    rating = models.FloatField(default=0.0)
    poster_url = models.URLField(blank=True)
    tmdb_id = models.PositiveIntegerField(
        null=True,
        blank=True,
        unique=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class Watchlist(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="watchlist_items"
    )
    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE,
        related_name="watchlisted_by"
    )
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-added_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["user", "movie"],
                name="unique_user_watchlist_movie"
            )
        ]

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"
