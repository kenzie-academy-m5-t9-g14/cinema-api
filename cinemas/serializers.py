from django.forms import NullBooleanField
from addresses.models import Address
from addresses.serializers import AddressCinemaSerializer, AddressSerializer
from rest_framework import serializers
import ipdb
from cinemas.models import Cinema


class CinemaSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
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
        
class CinemaUpdateSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    class Meta:
        model = Cinema
        fields = ['id', 'name', 'phone', 'email', 'opening_hours', 'address','status_active']
        read_only_fields = ["user"]

    def update(self, instance: Cinema, validated_data:dict):
        if validated_data.get('address'):
            address_poped = validated_data.pop('address')

            verificated_address, _ = Address.objects.get_or_create(**address_poped)
            instance.address = verificated_address

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance