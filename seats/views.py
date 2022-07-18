from django.shortcuts import get_object_or_404
from rest_framework.views import  Response, status
from rest_framework import generics
from movie_theaters.models import MovieTheater
from .models import  Seat
from .serializers import  SeatMapSerializer, SeatSerializer


class SeatView(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatMapSerializer

    def perform_create(self, serializer):
        movie_theater = get_object_or_404(MovieTheater ,pk = self.kwargs.get("pk"))
        return serializer.save(movie_theater=movie_theater)


        # seats_data = validated_data.pop("seatMap")
    
        #  seats_list = []
        #  for seat in seats_data:
        #      seat2,_ = Seat.objects.get_or_create(**seat,movie_theater = movie_theater)
        #      seats_list.append(seat2)

        #  seat_map = SeatMap.objects.create(**validated_data)
        #  seat_map.seats.set(seats_list)
        #  return seat_map 
    
    # def create(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = authenticate(
    #     username=serializer.validated_data["email"],
    #     password=serializer.validated_data["password"],
    #     )
    #     if user:
    #       token, _ = Token.objects.get_or_create(user=user)
    #       headers = self.get_success_headers(serializer.data)
    #       token = token.key
    #       return Response({"token": token}, status=status.HTTP_201_CREATED, headers=headers)
    #     return Response(
    #         {"detail": "Invalid email or password"}, status.HTTP_401_UNAUTHORIZED 
    #     )    

class SeatDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer






