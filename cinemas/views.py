from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

from cinemas.permissions import CustomAdminPermission
from cinemas.serializers import CinemaSerializer

from cinemas.models import Cinema

class CinemaView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # {CustomAdminPermission]

    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

class CinemaDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, CustomAdminPermission]

    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer



