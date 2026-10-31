
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .models import Movie, Watchlist
from .recommendations import (
    get_recommendations,
    get_personalized_recommendations,
)


def home(request):
    movies = Movie.objects.all()

    selected_movie = None
    recommendations = []
    best_matches = []
    discover = []

    movie_id = request.GET.get("movie")

    if movie_id:
        try:
            movie_id = int(movie_id)
            selected_movie = get_object_or_404(Movie, id=movie_id)
            recommendations = get_recommendations(movie_id)
        except (ValueError, TypeError):
            selected_movie = None

    if request.method == "POST":
        favorite_genres = request.POST.getlist("genres")
        favorite_movie_id = request.POST.get("favorite_movie") or None

        if favorite_movie_id:
            try:
                favorite_movie_id = int(favorite_movie_id)
            except (ValueError, TypeError):
                favorite_movie_id = None

        results = get_personalized_recommendations(
            favorite_genres=favorite_genres,
            favorite_movie_id=favorite_movie_id,
        )

        best_matches = results["best_matches"]
        discover = results["discover"]

    context = {
        "movies": movies,
        "selected_movie": selected_movie,
        "recommendations": recommendations,
        "best_matches": best_matches,
        "discover": discover,
        "genre_choices": Movie.GENRE_CHOICES,
    }

    return render(request, "movies/home.html", context)


def signup_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Welcome to CineMatch!")
            return redirect("home")
    else:
        form = UserCreationForm()

    return render(request, "movies/signup.html", {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Welcome back!")
            next_url = request.GET.get("next", "")
            if next_url.startswith("/") and not next_url.startswith("//"):
                return redirect(next_url)
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "movies/login.html", {"form": form})


@require_POST
def logout_view(request):
    logout(request)
    messages.success(request, "You have logged out.")
    return redirect("home")


@login_required
@require_POST
def add_to_watchlist(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    _, created = Watchlist.objects.get_or_create(
        user=request.user,
        movie=movie,
    )

    if created:
        messages.success(request, f"{movie.title} added to your watchlist.")
    else:
        messages.info(request, f"{movie.title} is already in your watchlist.")

    return redirect(request.POST.get("next") or "home")


@login_required
def watchlist_view(request):
    items = Watchlist.objects.filter(user=request.user).select_related("movie")
    return render(request, "movies/watchlist.html", {"items": items})


@login_required
@require_POST
def remove_from_watchlist(request, movie_id):
    Watchlist.objects.filter(
        user=request.user,
        movie_id=movie_id,
    ).delete()

    messages.success(request, "Movie removed from your watchlist.")
    return redirect("watchlist")
