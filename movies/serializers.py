from rest_framework import serializers
from movies.models import MoviesModel
from genres.serializers import GenreSerializer
from genres.models import Genre
import ipdb



class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = MoviesModel

        fields = ["id","name","duration","parental_rating","sinopse","imdb_rating","release_date","closing_date","created_at","updated_at","genres"]
        extra_kwargs = {"id":{"read_only":True},"created_at":{"read_only":True}, "updated_at":{"read_only":True}}

        


    def create(self,validated_data):
        genre = validated_data.pop("genres")

        new_genre = [Genre.objects.get_or_create(name=item["name"])[0] for item in genre]

        movie = MoviesModel.objects.create(**validated_data)


        movie.genres.set(new_genre)

        return movie


    def update(self,instance:MoviesModel,validated_data):

        if validated_data.get("genres"):
            genre = validated_data.pop("genres") # aqui eu corto o genre
            new_genre = [Genre.objects.get_or_create(name=item["name"])[0] for item in genre]
            instance.genres.set(new_genre) 
               


        for key, value in validated_data.items():

            setattr(instance,key,value)

        return instance

