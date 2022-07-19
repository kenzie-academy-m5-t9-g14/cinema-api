from cinemas.models import Cinema
from cinemas.serializers import CinemaSerializer, CinemaSerializerDetails
from rest_framework import serializers

from .models import MovieTheater


class MovieTheaterSerializer(serializers.ModelSerializer):
    cinema = CinemaSerializer(read_only=True)

    class Meta:
        model = MovieTheater
        fields = ['cinema', 'id', 'name', 'type', 'number_of_seats', 'exhibit_type', 'created_at', 'updated_at', 'seats_id']
        read_only_fields  = ['id','seats_id', 'created_at', 'updated_at']

    def create(self, validated_data):
        return MovieTheater.objects.create(**validated_data)

class ListCinemaMovieTheaters(serializers.ModelSerializer):
      
    class Meta:
        model = Cinema
        fields = ['id', 'name', 'movie_theathers']
        depth = 1
        
class ListAllMovieTheaters(serializers.ModelSerializer):
    cinema = CinemaSerializerDetails(read_only=True)
    
    class Meta:
        model = MovieTheater
        fields = ['cinema','id', 'name', 'type']
        
    
    