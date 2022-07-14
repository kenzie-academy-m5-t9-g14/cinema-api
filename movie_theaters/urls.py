from django.urls import path

from .views import ListTheaterView, MovieTheaterDetailView, MovieTheaterView

urlpatterns = [
    path("movie_theaters/", ListTheaterView.as_view()),
    path("movie_theaters/cinema/<cinema_id>/", MovieTheaterView.as_view()),
    path("movie_theaters/<pk>/", MovieTheaterDetailView.as_view())
]