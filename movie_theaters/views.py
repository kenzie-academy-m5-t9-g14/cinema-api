from cinemas.models import Cinema
from movie_sessions.models import MovieSession
from movie_sessions.serializers import MovieSessionSerializer
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from movie_theaters.permissions import CustomAdminPermission
from movie_theaters.serializers import (ListAllMovieTheaters,
                                        ListCinemaMovieTheaters,
                                        MovieTheaterSerializer)

from .models import MovieTheater


class MovieTheaterView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, CustomAdminPermission]
    
    queryset = MovieTheater.objects.all()
    serializer_class = MovieTheaterSerializer
    
    def perform_create(self, serializer):
        return serializer.save(cinema_id=self.kwargs.get('cinema_id'))
    
class ListTheaterView(generics.ListAPIView):
    queryset = MovieTheater.objects.all()
    serializer_class = ListAllMovieTheaters


class MovieTheaterDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, CustomAdminPermission]
    
    queryset = MovieTheater.objects.all()
    serializer_class = MovieTheaterSerializer
    
        
class ListAllCinemasSameMovieTheaterView(generics.RetrieveAPIView):
    queryset = Cinema.objects.all()
    serializer_class = ListCinemaMovieTheaters
    
    lookup_url_kwarg = "cinema_id"

