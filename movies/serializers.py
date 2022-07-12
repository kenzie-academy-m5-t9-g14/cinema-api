from rest_framework import serializers
from movies.models import MoviesModel


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = MoviesModel
        fields = "__all__"
        