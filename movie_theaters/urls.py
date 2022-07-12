from django.urls import path

from .views import MovieTheaterDetailView, MovieTheaterView

urlpatterns = [
    path("movie_theaters/", MovieTheaterView.as_view()),
    path("movie_theaters/<pk>/", MovieTheaterDetailView.as_view())
]