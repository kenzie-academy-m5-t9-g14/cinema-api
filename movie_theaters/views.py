from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


from movie_theaters.permissions import CustomAdminPermission
from movie_theaters.serializers import MovieTheaterSerializer

from .models import MovieTheater


from movie_sessions.models import MovieSession

class MovieTheaterView(generics.CreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    
    queryset = MovieTheater.objects.all()
    serializer_class = MovieTheaterSerializer
    
    def perform_create(self, serializer):
        return serializer.save(cinema_id=self.kwargs.get('cinema_id'))
    
class ListTheaterView(generics.ListAPIView):
    queryset = MovieTheater.objects.all()
    serializer_class = MovieTheaterSerializer
    

class MovieTheaterDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    queryset = MovieTheater.objects.all()
    serializer_class = MovieTheaterSerializer

