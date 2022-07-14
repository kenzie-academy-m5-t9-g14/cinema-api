from cinemas.serializers import CinemaSerializer
from rest_framework import serializers

from .models import MovieTheater
from movie_sessions.serializers import MovieSessionSerializer

class MovieTheaterSerializer(serializers.ModelSerializer):
    cinema = CinemaSerializer(read_only=True)

    class Meta:
        model = MovieTheater
        fields = ['id', 'name', 'type', 'number_of_seats', 'exhibit_type', 'created_at', 'updated_at', 'seats_id', 'cinema']
        read_only_fields  = ['id','seats_id', 'created_at', 'updated_at']


    def create(self, validated_data):
        return MovieTheater.objects.create(**validated_data)

