from django.shortcuts import get_object_or_404
from rest_framework.views import  Response, status
from rest_framework import generics
from movie_theaters.models import MovieTheater
from .mixins import SerializerByMethodMixin
from .models import  Seat
from .serializers import  SeatIdSerializer, SeatMapSerializer, SeatSerializer
from rest_framework.authentication import TokenAuthentication
from seats.permissions import CustomAdminPermission


class SeatView(SerializerByMethodMixin,generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomAdminPermission]
    queryset = Seat.objects.all()
    serializer_map = {
        "GET": SeatIdSerializer,
        "POST": SeatMapSerializer,
    }

    def perform_create(self, serializer):
        movie_theater = get_object_or_404(MovieTheater ,pk = self.kwargs.get("pk"))
        return serializer.save(movie_theater=movie_theater)

    def list(self, request, *args, **kwargs):
       queryset = self.filter_queryset(self.get_queryset())
       movie_theater = get_object_or_404(MovieTheater ,pk = self.kwargs.get("pk"))
       queryset = queryset.filter(movie_theater = movie_theater)
       page = self.paginate_queryset(queryset)
       if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

       serializer = self.get_serializer(queryset, many=True)
       return Response(serializer.data)    

class SeatListView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomAdminPermission]
    queryset = Seat.objects.all()
    serializer_class = SeatIdSerializer


class SeatDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [CustomAdminPermission]
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        setattr(instance,"status_active",False)
        instance.save()
        serializer = SeatSerializer(instance,{"status_active":False},partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_204_NO_CONTENT)






