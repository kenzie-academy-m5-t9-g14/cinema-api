from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers
from genres.models import Genre
from django.forms.models import model_to_dict



class MovieView(generics.ListCreateAPIView):
    queryset = models.MoviesModel.objects.all()
    serializer_class = serializers.MovieSerializer


    def perform_create(self, serializer):
        genres_capture = self.request.data.get("genres")
        new_genre = Genre.objects.get_or_create(name=genres_capture)[0]
        dicionario = {"id":new_genre.id,"name":new_genre.name}
        print(dicionario)


        serializer.save(genres = dicionario)
class MovieViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MoviesModel.objects.all()
    serializer_class = serializers.MovieSerializer

