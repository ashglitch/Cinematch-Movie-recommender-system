
from django.contrib import admin
from django.urls import path
from movies import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("signup/", views.signup_view, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("watchlist/", views.watchlist_view, name="watchlist"),
    path(
        "watchlist/add/<int:movie_id>/",
        views.add_to_watchlist,
        name="add_to_watchlist",
    ),
    path(
        "watchlist/remove/<int:movie_id>/",
        views.remove_from_watchlist,
        name="remove_from_watchlist",
    ),
]
