from rest_framework import serializers
from .models import Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street', 'district', 'number', 'city', 'zipcode']
        fields_read_only = ['id']