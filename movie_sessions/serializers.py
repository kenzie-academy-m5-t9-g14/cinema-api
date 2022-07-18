from rest_framework import serializers
from .models import MovieSession

class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at', 'movie', 'movie_theater']
