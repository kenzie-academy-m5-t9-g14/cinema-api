from django.shortcuts import get_object_or_404, render
from rest_framework import generics



from .models import MovieSession
from .serializers import MovieSessionSerializer

class MovieSessionView(generics.ListCreateAPIView):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer
    
    def perform_create(self, serializer):
        return serializer.save(movie_id=self.kwargs.get('movie_id'), movie_theater_id=self.kwargs.get('movie_theater_id'))
