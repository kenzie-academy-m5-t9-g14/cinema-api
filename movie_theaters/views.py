from rest_framework import generics

from movie_theaters.serializers import MovieTheaterSerializer

from .models import MovieTheater


class MovieTheaterView(generics.ListCreateAPIView):
    queryset = MovieTheater.objects.all()
    serializer_class = MovieTheaterSerializer
    
    def perform_create(self, serializer):
        return serializer.save(cinema=self.kwargs.get('cinema_id'))
    

class MovieTheaterDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieTheater.objects.all()
    serializer_class = MovieTheaterSerializer
