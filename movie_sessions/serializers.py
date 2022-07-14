from rest_framework import serializers
from .models import MovieSession

class MovieSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieSession
        fields = ['id', 'exhibit_type', 'price', 'created_at', 'updated_at', 'movie', 'seat', 'schedule']
        read_only_fields = ['created_at', 'updated_at']
