import uuid
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import serializers
import movie_sessions
from movie_sessions.serializers import MovieSessionSerializer
from movie_theaters.models import MovieTheater
from .mailing.utils import sendEmail
from payment_types.models import PaymentType
from payment_types.serializers import PaymentTypeSerializer
from seats.models import Seat
from seats.serializers import   SeatSerializer
from users.models import User
from .models import  Ticket 
from users.serializers import UserSerializer


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
         seats_list_movie_theater = validated_data["movie_session"].movie_theater.seats.all()
         for seat in seat_map_data:
            found = False
            for seat_movie_theater in seats_list_movie_theater:
               if seat_movie_theater.row == seat["row"] and seat_movie_theater.seat == seat["seat"]:
                 found =True
                 break
            if not found:
                raise Http404

         payment_type,_ = PaymentType.objects.get_or_create(**payment_type_data)
         ticket = Ticket.objects.create(**validated_data,payment_type=payment_type)
         ticket.seats.set(seat_map_data)
         email = ticket.buyer.email
         subject = "Compra de ingresso efetuada com sucesso"
         message = f"Parabéns pela compra, {ticket.buyer.name}\n Sua sessão de cinema está confirmada em: \n {ticket.movie_session.movie_theater.cinema.name}, Sala: {ticket.movie_session.movie_theater.name}, sessão: {ticket.movie_session.movie_theater.type}, {ticket.movie_session.movie_theater.exhibit_type}\n Para o filme: {ticket.movie_session.movie.name} \n No dia : {ticket.movie_session.schedule.all()[0].date} , as: {ticket.movie_session.schedule.all()[0].hour}  "
         if ticket:
             sendEmail(subject,message,[email])
         return ticket    

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id','buyer', 'created_at','is_student','payment_type','total_value','status_active','updated_at']
        depth = 0

