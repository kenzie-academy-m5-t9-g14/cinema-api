from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import Response,status
from cinemas.mixins import SerializerByMethodMixin
from cinemas.models import Cinema
from cinemas.permissions import CustomAdminPermission
from cinemas.serializers import CinemaSerializer, CinemaSerializerList


class CinemaView(SerializerByMethodMixin, generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, CustomAdminPermission]

    queryset = Cinema.objects.all()
    serializer_map = {
        "GET":  CinemaSerializerList,
        "POST":CinemaSerializer,    
    }

class CinemaDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, CustomAdminPermission]

    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        setattr(instance,"status_active",False)
        instance.save()
        serializer = CinemaSerializer(instance,{"status_active":False},partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_204_NO_CONTENT)



