from addresses.models import Address
from addresses.serializers import AddressCinemaSerializer, AddressSerializer
from rest_framework import serializers

from cinemas.models import Cinema


class CinemaSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    class Meta:
        model = Cinema
        fields = ['id', 'name', 'phone', 'email', 'opening_hours', 'address','status_active']
        read_only_fields = ["user"]

    def create(self, validated_data):
        address_instance = Address.objects.create(**validated_data.pop("address"))
        return Cinema.objects.create(**validated_data, address=address_instance)

class CinemaSerializerDetails(serializers.ModelSerializer):
    
    class Meta:
        model = Cinema
        fields = ['id', 'name']
        read_only_fields = ["user"]

class CinemaSerializerList(serializers.ModelSerializer):

    address = AddressCinemaSerializer() 
    class Meta:
        model = Cinema
        fields = ['id','name','address']
        read_only_fields = ["user"]
        
