from rest_framework import serializers
from movies.models import MoviesModel
from genres.serializers import GenreSerializer

class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(read_only = True)
    class Meta:
        model = MoviesModel
        # fields = "__all__"
        fields = ["id","name","duration","parental_rating","sinopse","imdb_rating","release_date","closing_date","created_at","updated_at","genres"]
        extra_kwargs = {"id":{"read_only":True},"created_at":{"read_only":True}, "updated_at":{"read_only":True},"genres":{"read_only":True}}
        # depth = 1
        