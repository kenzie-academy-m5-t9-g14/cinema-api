from django.urls import path

from . import views

urlpatterns = [
path("kinema/movies/", views.MovieView.as_view()),
path("kinema/movies/<pk>/", views.MovieViewDetail.as_view())
]
