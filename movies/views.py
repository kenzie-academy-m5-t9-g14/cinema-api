from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers





class MovieView(generics.ListCreateAPIView):
    queryset = models.MoviesModel.objects.all()
    serializer_class = serializers.MovieSerializer


class MovieViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MoviesModel.objects.all()
    serializer_class = serializers.MovieSerializer