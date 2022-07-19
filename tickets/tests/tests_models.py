from django.test import TestCase
from django.db import models
from cinemas.models import Cinema
from movie_theaters.models import MovieTheater
from movies.models import MoviesModel
from genres.models import Genre
from users.models import User
from addresses.models import Address
import uuid

class MovieModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.payment_type    = {"type":"credito"}
        cls.total_value       = 35.00
        cls.seats = [{"row":"A", "seat":"1"},{"row":"A", "seat":"2"}]
        
        cls.address_user_data = {
                "street":"rua mockup",
		        "district": "district",
		        "number": 100,
		        "zipcode":"1597536",
		        "city":"bauru"
        }

        cls.address_cinema_data = {
                "street":"rua exemplo",
		        "district": "cine ma",
		        "number": 49,
		        "zipcode":"36555563",
		        "city":"bauru"
        }

        cls.address_user = Address.objects.create(**cls.address_user_data)
        cls.address_cinema = Address.objects.create(**cls.address_cinema_data)

        cls.superuser_data = {
            "name": "super user", 
            "password": "senha_forte",
            "email":"super@user.com",
            "birth_date":"2000-4-03",
            "address_id":cls.address.id
        }
        
        cls.superuser = User.objects.create_superuser(**cls.superuser_data)

        cls.cinema_data = {
              "name":"Daslu2",
	          "phone":"434725566",
	          "email":"daslu@gmail.com",
	          "opening_hours": "10:00 - 21:00",
              "owner":cls.superuser
        }

        cls.cinema = Cinema.objects.create(**cls.cinema_data)

        cls.movie_theaters_data = {
            "name":"Sala 2",
            "type":"3D",
            "number_of_seats":"60",
            "exhibit_type":"Legendado",
            "cinema_id" : cls.cinema.id
        }

        cls.movie_theaters = Cinema.objects.create(**cls.movie_theaters_data)

        cls.seat = {
             "row": "A",
             "seat": "2",
             "is_active":True ,
             "movie_theater": cls.movie_theaters
        }

        cls.movie_theaters = MovieTheater.objects.create(**cls.movie_theaters_data)

        cls.movie_data = {
               "name":"Senhor dos Aneis",
               "duration": "250 min ",
               "parental_rating": "14",
               "sinopse":"Um velho barbudo e sua turminha do barulho",
               "imdb_rating": "7.9",
               "release_date":"2022-01-12",
               "closing_date": "2022-03-12",
               "genres":  [{"name":"Ficção"},{"name":"Fantasia"}]
        }

        cls.movie = MoviesModel.objects.create(**cls.movie_data)

        session_data = {
            
        }

        id = models.UUIDField(
            primary_key = True, 
            default = uuid.uuid4,
            editable = False
         )
        exhibit_type = models.CharField(max_length=30)
        price = models.DecimalField(max_digits=15, decimal_places=2)
        created_at = models.DateTimeField(default=timezone.now)
        updated_at = models.DateTimeField(default=timezone.now)
    
        movie = models.ForeignKey("movies.MoviesModel", on_delete=models.CASCADE, related_name="movie_sessions")
        movie_theater = models.ForeignKey("movie_theaters.MovieTheater", on_delete=models.CASCADE, related_name="movie_sessions")
        schedule = models.ManyToManyField("schedules.Schedule", related_name="sessions", null=True)


   

        #movie session
   

        
 
            

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
