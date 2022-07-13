from rest_framework import serializers
from .models import Schedule

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['id', 'hour','date', 'created_at', 'updated_at']
        read_only_fields = ['id','created_at', 'updated_at']