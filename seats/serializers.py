from builtins import int
import collections
from typing import OrderedDict
from rest_framework import serializers
from traitlets import Integer
from movie_theaters.models import MovieTheater
from movie_theaters.serializers import MovieTheaterSerializer
from seats.models import Seat, SeatMap

class SeatSerializer(serializers.ModelSerializer):
    movie_theater = MovieTheaterSerializer(read_only=True)
    class Meta:
        model = Seat
        fields = "__all__"

class SeatMapSerializer(serializers.ModelSerializer):
    seatMap = SeatSerializer(many=True)

    class Meta:
       model = SeatMap
       fields = "__all__"

    def create(self, validated_data:dict):
         seats_data = validated_data.pop("seatMap")
         seat_list = []
         rows_list = []
         for seats in seats_data:
             seat_list.append(seats["seat"])
             rows_list.append(seats["row"])
         movie_theater = validated_data.pop("movie_theater")
         movie_theater = MovieTheater.objects.get(name = movie_theater.name)    

         seats_list = []
         for row in rows_list:
            for seat in seat_list:
                num = int(seat)
                while num > 0:
                   dict = {"row":str(num),"seat":row} 
                   num -=1
                   print(dict) 
                   seat2,_ = Seat.objects.get_or_create(**dict,movie_theater = movie_theater)
                   seats_list.append(seat2)  
                break    
                               
         seat_map = SeatMap.objects.create(**validated_data)
         seat_map.seatMap.set(seats_list)
         return seat_map 

