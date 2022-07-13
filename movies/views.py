from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers
from genres.models import Genre
from django.forms.models import model_to_dict
import ipdb


class MovieView(generics.ListCreateAPIView):
    queryset = models.MoviesModel.objects.all()
    serializer_class = serializers.MovieSerializer


    # def perform_create(self, serializer):
    #     genres_capture = self.request.data.get("genres")
    #     # for item in genres_capture:
    #         # new_genre = Genre.objects.get_or_create(name=item.name)[0]
    #     # # new_genre = Genre.objects.get_or_create(name=genres_capture["name"])[0]
    #     # dicionario = {"id":new_genre.id,"name":new_genre.name}
    #     # print(dicionario)
    #     # new_genre = [Genre.objects.get_or_create(name=item["name"])[0] for item in genres_capture]
    #     # ipdb.set_trace()

    #     # serializer.save(genres=new_genre)
class MovieViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.MoviesModel.objects.all()
    serializer_class = serializers.MovieSerializer



# To do:
# alterar a forma que eu recebo miha requisição