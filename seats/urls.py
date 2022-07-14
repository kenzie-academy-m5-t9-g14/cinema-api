from django.urls import path

from . import views

urlpatterns = [
    path("movie_theaters/<int:movie_theater_id/seats", views.SeatsCreateView.as_view())

]