
from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title", "genre", "year", "rating")
    list_filter = ("genre", "year")
    search_fields = ("title", "description")
