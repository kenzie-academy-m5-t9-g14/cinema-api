from django.test import TestCase
from rest_framework.authtoken.models import Token


from movie_theaters.models import MovieTheater
from users.models import User
from cinemas.models import Cinema
from addresses.models import Address


class MovieTheaterModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        cls.superuser = User.objects.create_superuser(**{"name": "Gabriel", "password": "1234","email":"gabriel@admin.com","birth_date":"2022-02-02"})

        cls.token = Token.objects.create(user = cls.superuser)

        cls.cinema = Cinema.objects.create( name="Daslu2", phone="434725566", email="daslu@gmail.com",opening_hours= "10:00 - 21:00", address = Address.objects.create(
		 street="Columbia",
		 district="Laranjeiras",
		 number=159,
		 city="Houston",
		 zipcode="86444222"
   ))

        cls.movie_theater = MovieTheater.objects.create(
            name="Sala 5",
            type="2D",
            number_of_seats="30",
            exhibit_type="Dublado",
            cinema_id = cls.cinema.id
            )
  

        

    def test_name_exists(self):
        name = self.movie_theater._meta.get_field("name")
        self.assertIsNotNone(name)


    def test_cinema_id_in_movie_theater(self):
        uuid = self.cinema.id

        self.assertEqual(uuid, self.movie_theater.cinema_id)