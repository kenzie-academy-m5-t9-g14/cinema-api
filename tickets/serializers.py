from rest_framework import serializers

from payment_types.models import PaymentType
from payment_types.serializers import PaymentTypeSerializer
from users.models import User
from .models import  Ticket 
from users.serializers import UserSerializer

#movie_session,payment_type

class TicketDetailSerializer(serializers.ModelSerializer):
    buyer = UserSerializer(read_only=True)
    payment_type = PaymentTypeSerializer()
    class Meta:
        model = Ticket
        fields = ['id','buyer', 'created_at','is_student','payment_type','total_value','status_active','updated_at']
        read_only_fields = ['buyer','created_at','updated_at']
        

    def create(self, validated_data:dict):
         payment_type_data = validated_data.pop("payment_type") 
         payment_type,_ = PaymentType.objects.get_or_create(**payment_type_data)
         ticket = Ticket.objects.create(**validated_data,payment_type=payment_type)
         return ticket    

class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = ['id','buyer', 'created_at','is_student','payment_type','total_value','status_active','updated_at']

 