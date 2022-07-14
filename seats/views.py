from imp import get_frozen_object
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication


from . import serializers
from . import models
from . import permissions

from movie_theaters.models import MovieTheater

class SeatsCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.AuthPermissionToUser]

    def post(self, request, movie_theater_id):

        movie_theater = get_object_or_404(MovieTheater, id = movie_theater_id)

        serializer = serializers.SeatSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(movie = movie_theater)

        return Response(serializer.data, status = status.HTTP_201_CREATED)
        



        
