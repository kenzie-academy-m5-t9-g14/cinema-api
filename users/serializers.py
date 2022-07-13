from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    email = serializers.EmailField()

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}


    def validate_email(self, value):
        
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError(detail =["email already exists"])
        
        return value


    def create(self, validated_data):

        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)