from dataclasses import fields
from rest_framework import serializers
from seats.models import Seat
from schedules.serializers import ScheduleSerializer
from movie_theaters.serializers import MovieTheaterSerializer
from movie_theaters.models import MovieTheater

class SeatSerializer(serializers.ModelSerializer):
    movie_theater_id = MovieTheaterSerializer(read_only = True)
    class Meta:
        model = Seat
        # fields = "__all__"
        fields = ["id","row","seat","availability","movie_theater_id"]


    

        