from addresses.models import Address
from addresses.serializers import AddressSerializer
from rest_framework import serializers

from .models import User


class UserAdminSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    address = AddressSerializer()
    class Meta:
        model = User
        fields = ['id', 'name', 'cpf', 'email', 'birth_date', 'cellphone', 'genre', 'address', 'password','status_active']
        extra_kwargs = {'password': {'write_only': True}}


    def validate_email(self, value):
        
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError(detail =["email already exists"])
        
        return value


    def create(self, validated_data):
        address_poped = validated_data.pop('address')
        validated_address, _ = Address.objects.get_or_create(**address_poped)

        user = User.objects.create_superuser(**validated_data, address=validated_address)
        
        return user

    def update(self, instance: User, validated_data:dict):
        if validated_data.get('address'):
            address_poped = validated_data.pop('address')

            verificated_address, _ = Address.objects.get_or_create(**address_poped)
            instance.address = verificated_address

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()
    address = AddressSerializer()

    class Meta:
        model = User
        fields = ['id', 'name', 'cpf', 'email', 'birth_date', 'cellphone', 'genre', 'address', 'password','status_active']
        extra_kwargs = {'password': {'write_only': True}}


    def validate_email(self, value):
        
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError(detail =["email already exists"])
        
        return value


    def create(self, validated_data):
        address_poped = validated_data.pop('address')
        validated_address, _ = Address.objects.get_or_create(**address_poped)

        user = User.objects.create_user(**validated_data, address=validated_address)
        
        return user      

    def update(self, instance: User, validated_data:dict):
        if validated_data.get('address'):
            address_poped = validated_data.pop('address')

            verificated_address, _ = Address.objects.get_or_create(**address_poped)
            instance.address = verificated_address

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance  


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'cpf', 'email']


class SpecificUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}

        
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
