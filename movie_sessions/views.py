from rest_framework import generics
from rest_framework.views import  Response, status

from .models import MovieSession
from .serializers import MovieSessionSerializer

from django.utils import timezone

class MovieSessionView(generics.ListCreateAPIView):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer
    
    def perform_create(self, serializer):
        return serializer.save(movie_id=self.kwargs.get('movie_id'), movie_theater_id=self.kwargs.get('movie_theater_id'))

class MovieSessionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        setattr(instance,"status_active",False)
        setattr(instance,"updated_at",timezone.now())
        instance.save()
        serializer = MovieSessionSerializer(instance,{"status_active":False},partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_204_NO_CONTENT)

