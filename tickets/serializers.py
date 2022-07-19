from django.shortcuts import get_object_or_404
from rest_framework import serializers
import movie_sessions
from movie_sessions.serializers import MovieSessionSerializer

from payment_types.models import PaymentType
from payment_types.serializers import PaymentTypeSerializer
from seats.models import Seat
from seats.serializers import   SeatSerializer
from users.models import User
from .models import  Ticket 
from users.serializers import UserSerializer

#movie_session

class TicketDetailSerializer(serializers.ModelSerializer):
    buyer = UserSerializer(read_only=True)
    movie_session = MovieSessionSerializer(read_only=True)
    payment_type = PaymentTypeSerializer()
    seats = SeatSerializer(many=True)

    class Meta:
        model = Ticket
        fields = ['id','buyer', 'created_at','is_student','payment_type','total_value','status_active','updated_at','movie_session','seats']
        read_only_fields = ['buyer','created_at','updated_at']  

    def create(self, validated_data:dict):
         payment_type_data = validated_data.pop("payment_type")
         seat_map_data = validated_data.pop("seats")
         seats_list = []

         #new_genre = [Genre.objects.get_or_create(name=item["name"])[0] for item in genre]
        
         for seat in seat_map_data:
            #seat2 = Seat.objects.get(id = seat["ticket_seat_id"])  
            seat2 = get_object_or_404(Seat ,row = seat["row"],seat= seat['seat'])
            print(seat2,'2')
            seats_list.append(seat2)
         payment_type,_ = PaymentType.objects.get_or_create(**payment_type_data)
         ticket = Ticket.objects.create(**validated_data,payment_type=payment_type)
         print(vars(ticket))
         ticket.seats.set(seats_list)
         
         return ticket    

class TicketSerializer(serializers.ModelSerializer):


    class Meta:
        model = Ticket
        fields = ['id','buyer', 'created_at','is_student','payment_type','total_value','status_active','updated_at']

