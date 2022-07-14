from rest_framework import generics

from movie_theaters.serializers import MovieTheaterSerializer, MovieTheaterMovieSessionsSerializer
from .models import MovieTheater

from movie_sessions.models import MovieSession
from movie_sessions.serializers import MovieSessionSerializer

class MovieTheaterView(generics.ListCreateAPIView):
    queryset = MovieTheater.objects.all()
    serializer_class = MovieTheaterSerializer
    

class MovieTheaterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieTheater.objects.all()
    serializer_class = MovieTheaterSerializer


class MovieTheaterMovieSessionsView(generics.ListCreateAPIView):
    queryset = MovieSession.objects.all()
    serializer_class = MovieTheaterMovieSessionsSerializer