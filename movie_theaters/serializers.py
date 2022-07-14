from rest_framework import serializers

from .models import MovieTheater
from movie_sessions.serializers import MovieSessionSerializer

class MovieTheaterSerializer(serializers.ModelSerializer):
    # session = SessionSerializer(read_only=True)

    class Meta:
        model = MovieTheater
        fields = ['id','name', 'type', 'number_of_seats', 'exhibit_type', 'created_at', 'updated_at']
        read_only_fields  = ['id','seats_id', 'created_at', 'updated_at']
        extra_kwargs = {'password': {"write_only": True}}


class MovieTheaterMovieSessionsSerializer(serializers.ModelSerializer):
    movie_sessions = MovieSessionSerializer()

    class Meta:
        fields = ['movie_sessions']
