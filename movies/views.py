from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication

from . import models
from . import serializers
from . import permissions

from django.forms.models import model_to_dict



class MovieView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.AuthPermissionToUser]

    queryset = models.MoviesModel.objects.all()
    serializer_class = serializers.MovieSerializer


class MovieViewDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.AuthPermissionToUser]

    queryset = models.MoviesModel.objects.all()
    serializer_class = serializers.MovieSerializer

