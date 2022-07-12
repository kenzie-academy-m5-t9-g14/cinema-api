from django.urls import path
from movies.views import MovieView, MovieViewDetail



urlpatterns = [
path("kinema/movies/", MovieView.as_view()),
path("kinema/movies/<pk>/", MovieViewDetail.as_view())
]