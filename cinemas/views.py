from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from cinemas.models import Cinema
from cinemas.permissions import CustomAdminPermission
from cinemas.serializers import CinemaSerializer


class CinemaView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, CustomAdminPermission]

    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

class CinemaDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, CustomAdminPermission]

    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer



