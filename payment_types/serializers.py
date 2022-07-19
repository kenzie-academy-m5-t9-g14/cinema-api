from rest_framework import serializers
from .models import PaymentType

class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ['id', 'type', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at',"id"]