from django.urls import path

from . import views

urlpatterns = [
    path("movie_theaters/", views.ListTheaterView.as_view()),
    path("movie_theaters/cinema/<cinema_id>/movie_theater/", views.MovieTheaterView.as_view()),
    path("movie_theaters/<pk>/", views.MovieTheaterDetailView.as_view()),
    path("movie_theaters/<cinema_id>/cinema/", views.ListAllCinemasSameMovieTheaterView.as_view())
]
