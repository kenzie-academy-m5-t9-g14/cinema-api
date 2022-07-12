from cinemas.serializers import CinemaSerializer
from rest_framework import generics

from cinemas.models import Cinema

class ListCreateCinemaView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

class RetrieveUpdateDestroyCinemaView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer



