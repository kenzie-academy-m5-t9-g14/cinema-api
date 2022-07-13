from rest_framework import serializers
from .models import Session

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ['id', 'exhibit_type', 'price', 'created_at', 'updated_at', 'movie', 'seat'] #schedule
        read_only_fields = ['created_at', 'updated_at']
