from cinemas.serializers import CinemaSerializer
from rest_framework import generics

from cinemas.models import Cinema

class CinemaView(generics.ListCreateAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

class CinemaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer



