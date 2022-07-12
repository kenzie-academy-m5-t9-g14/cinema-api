from django.urls import path

from .views import ListCreateMovieTheaterView, MovieTheaterDetailView

urlpatterns = [
    path("movie_theaters/", ListCreateMovieTheaterView.as_view()),
    path("movie_theaters/<pk>/", MovieTheaterDetailView.as_view())
]