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


class SeatIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Seat
        fields = "__all__"
        depth = 0        



class SeatMapSerializer(serializers.ModelSerializer):
    seatMap = SeatSerializer(many=True)

    class Meta:
       model = SeatMap
       fields = "__all__"

    def create(self, validated_data:dict):
         seats_data = validated_data.pop("seatMap")
         movie_theater = validated_data.pop("movie_theater")
         movie_theater = MovieTheater.objects.get(name = movie_theater.name)  
         seats_list = []
         for row_data in seats_data:       
            num = int(row_data["seat"])
            while num > 0:
                dict = {"row":row_data["row"],"seat": str(num)} 
                num -=1
                seat2,_ = Seat.objects.get_or_create(**dict,movie_theater = movie_theater)
                seats_list.append(seat2)  
                  
         seat_map = SeatMap.objects.create(**validated_data)
         seat_map.seatMap.set(seats_list)
         return seat_map

class SeatAvaibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ['id', 'row', 'seat']

