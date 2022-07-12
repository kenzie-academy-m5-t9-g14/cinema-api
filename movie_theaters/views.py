from rest_framework import generics

from movie_theaters.serializers import MovieTheaterSerializer
from .models import MovieTheater



class MovieTheaterView(generics.ListCreateAPIView):
    queryset = MovieTheater.objects.all()
    serializer_class = MovieTheaterSerializer
    

class MovieTheaterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieTheater.objects.all()
    serializer_class = MovieTheaterSerializer