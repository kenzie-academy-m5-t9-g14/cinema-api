from django.urls import path

from . import views

urlpatterns = [
    # path("movie_sessions/<pk>/seats/", views.MovieSessionAvaibleSeatsView.as_view()),
    path("movie_theater/<str:movieTheaterId>/movies/<str:movieId>/movie_sessions/<pk>/", views.MovieSessionDetailView.as_view()),
    path("movie_theater/<str:movie_theater_id>/movies/<str:movie_id>/movie_sessions/", views.MovieSessionView.as_view())
]