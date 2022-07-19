from django.test import TestCase
from movies.models import MoviesModel
from genres.models import Genre

class MovieModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.name            = "Senhor dos Aneis"
        cls.duration        = "250 min "
        cls.parental_rating = "14"
        cls.sinopse         = "Um velho barbudo e sua turminha do barulho"
        cls.imdb_rating     = "7.9"
        cls.release_date    = "2022-01-12"
        cls.closing_date    = "2022-03-12"
        cls.genres          =  [{"name":"Ficção"},{"name":"Fantasdia"}]

        
        cls.movie = MoviesModel.objects.create(
            name = cls.name,
            duration = cls.duration,
            parental_rating = cls.parental_rating,
            sinopse = cls.sinopse,
            imdb_rating = cls.imdb_rating,
            release_date = cls.release_date,
            closing_date = cls.closing_date
        )
            

    def test_name_description(self):
        uuid = self.movie.id
        new_movie = MoviesModel.objects.get(id= uuid)
        movie_name = new_movie._meta.get_field("name")
        self.assertIsNotNone(movie_name)

    def test_genres_description(self):
        uuid = self.movie.id
        new_movie = MoviesModel.objects.get(id= uuid)
        new_genre = [Genre.objects.get_or_create(name=item["name"])[0] for item in self.genres]
        new_movie.genres.set(new_genre)
        genre_atribute = new_movie._meta.get_field("genres")

        self.assertIsNotNone(genre_atribute)







