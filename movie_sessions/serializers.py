from rest_framework import serializers
from movie_theaters.models import MovieTheater
from movie_theaters.serializers import MovieTheaterSerializer
from movies.models import MoviesModel
from movies.serializers import MovieSerializer
from schedules.models import Schedule
from schedules.serializers import ScheduleSerializer
from seats.models import Seat

from .models import MovieSession
import ipdb

import ipdb

class MovieSessionSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer(many=True)
    movie = MovieSerializer(read_only=True)
    movie_theater = MovieTheaterSerializer(read_only=True)
    class Meta:
        model = MovieSession
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'movie', 'movie_theater','schedule']

    def create(self, validated_data):
           movie = validated_data.pop("movie_id")
           movie_theater = validated_data.pop("movie_theater_id")
           schedules = validated_data.pop("schedule")
           movie_theater_instance = MovieTheater.objects.get(id = movie_theater)  
           movie_instance = MoviesModel.objects.get(id = movie) 
           schedule_instances = [Schedule.objects.get_or_create(hour=item["hour"],date=item["date"])[0] for item in schedules]
           movie_session = MovieSession.objects.create(**validated_data,movie_theater = movie_theater_instance,movie=movie_instance)
           movie_session.schedule.set(schedule_instances)
           return movie_session

#class SeatsAvaibleSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Seat
#        fields = ['id', 'row', 'seat']
#
#
#class MovieSessionSeatsSerializer(serializers.ModelSerializer):
#    avaible_seats = SeatsAvaibleSerializer(many=True)
#    
#    class Meta:
#        model = MovieSession
#        fields = ['avaible_seats']

    



