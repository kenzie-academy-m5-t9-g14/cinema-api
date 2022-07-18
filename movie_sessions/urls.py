from django.urls import path

from . import views

urlpatterns = [
    path("movie_theater/<int:movie_theater_id>/movies/<int:movie_id>/movie_sessions/", views.MovieSessionsView.as_view())
]