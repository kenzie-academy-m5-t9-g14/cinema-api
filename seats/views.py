from django.shortcuts import get_object_or_404
from rest_framework.views import  Response, status
from rest_framework import generics
import movie_sessions
from movie_theaters.models import MovieTheater
from .models import  Seat
from .serializers import  SeatMapSerializer, SeatSerializer, SeatAvaibleSerializer

from movie_sessions.models import MovieSession
from tickets.models import Ticket

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


class SeatSessionView(generics.ListAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatAvaibleSerializer

    def get_queryset(self):
        movie_session_id = self.kwargs["movie_session_id"]
        movie_session = get_object_or_404(MovieSession ,pk = movie_session_id)
        movie_theater = movie_session.movie_theater
        tickets = Ticket.objects.filter(movie_session=movie_session)
        query_set = Seat.objects.filter(movie_theater=movie_theater)
        for e in tickets.all():
            for seat in e.seats.all():
                print("Seat id")
                print(seat.id)
                query_set = query_set.exclude(pk=seat.id)
        return query_set
