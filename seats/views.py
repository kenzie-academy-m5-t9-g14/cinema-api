from django.shortcuts import get_object_or_404
from rest_framework.views import  Response, status
from rest_framework import generics
from movie_theaters.models import MovieTheater
from .models import  Seat
from .serializers import  SeatMapSerializer, SeatSerializer


class SeatView(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatMapSerializer

    def perform_create(self, serializer):
        movie_theater = get_object_or_404(MovieTheater ,pk = self.kwargs.get("pk"))
        return serializer.save(movie_theater=movie_theater)


class SeatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        setattr(instance,"status_active",False)
        instance.save()
        serializer = SeatSerializer(instance,{"status_active":False},partial=True)
        serializer.is_valid(raise_exception=True)
        return Response(status=status.HTTP_204_NO_CONTENT)






