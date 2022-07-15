from django.urls import path

from .views import MovieTheaterDetailView, MovieTheaterView, MovieTheaterMovieSessionsView
urlpatterns = [
    path("movie_theaters/", MovieTheaterView.as_view()),
    path("movie_theaters/<pk>/", MovieTheaterDetailView.as_view()),
    path("movie_theaters/<pk>/movie_sessions/", MovieTheaterMovieSessionsView.as_view())
]