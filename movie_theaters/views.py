from rest_framework import generics

from movie_theaters.serializers import MovieTheaterSerializer, MovieTheaterMovieSessionsSerializer
from .models import MovieTheater

from rest_framework.authentication import TokenAuthentication

from movie_sessions.models import MovieSession

class MovieTheaterView(generics.ListCreateAPIView):
    queryset = MovieTheater.objects.all()
    serializer_class = MovieTheaterSerializer
    

class MovieTheaterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieTheater.objects.all()
    serializer_class = MovieTheaterSerializer


class MovieTheaterMovieSessionsView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    queryset = MovieSession.objects.all()
    serializer_class = MovieTheaterMovieSessionsSerializer