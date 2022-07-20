from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
import movie_theaters

from movie_theaters.models import MovieTheater
from users.models import User
from cinemas.models import Cinema
from addresses.models import Address


class MovieTheaterViewTests(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        cls.address = {
			"street":"Avenida Brazil",
		    "district": "Center",
		    "number": 84,
		    "zipcode":"85802120",
		    "city":"cascavel"
		}

        cls.address = Address.objects.create(**cls.address)

        cls.superuser = User.objects.create_superuser(**{"name": "Gabriel", "password": "1234","email":"gabriel@admin.com","birth_date":"2022-02-02", "address_id": cls.address.id})

        cls.token = Token.objects.create(user = cls.superuser)

        cls.cinema = Cinema.objects.create( name="Daslu2", phone="434725566", email="daslu@gmail.com",opening_hours= "10:00 - 21:00", address = Address.objects.create(
		 street="Columbia",
		 district="Laranjeiras",
		 number=159,
		 city="Houston",
		 zipcode="86444222"
   ))

        cls.movie_theater = {
            "name":"Sala 5",
            "type":"2D",
            "number_of_seats":"30",
            "exhibit_type":"Dublado",
            "cinema_id" : cls.cinema.id
        }

    def test_create_movie_theater(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)


        uuid = self.cinema.id
        if self.superuser.is_superuser:
            res = self.client.post(f'/kinema/movie_theaters/cinema/{uuid}/movie_theater/', data= self.movie_theater, format = "json")


        self.assertEqual(res.status_code,201)
        self.assertTrue(self.token.user.is_superuser)

    
    def test_list_movie_theater(self):
        
        res = self.client.get("/kinema/movie_theaters/")

        self.assertEqual(res.status_code, 200)


    def test_list_one_especific_movie_theater(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        uuid = self.cinema.id
        if self.superuser.is_superuser:
            movie_theater = self.client.post(f'/kinema/movie_theaters/cinema/{uuid}/movie_theater/', data= self.movie_theater, format = "json")

        res = self.client.get(f'/kinema/movie_theaters/{movie_theater.data["id"]}/')

    
    def test__patch_one_movie_theater(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        uuid = self.cinema.id
        if self.superuser.is_superuser:
                movie_theater = self.client.post(f'/kinema/movie_theaters/cinema/{uuid}/movie_theater/', data= self.movie_theater, format = "json")

        
        res = self.client.patch(f'/kinema/movie_theaters/{movie_theater.data["id"]}/', data= {"name": "new name"}, format = "json")


        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.data["name"], "new name")

    
    def test_delete_one_movie_theater(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        uuid = self.cinema.id
        if self.superuser.is_superuser:
            movie_theater = self.client.post(f'/kinema/movie_theaters/cinema/{uuid}/movie_theater/', data= self.movie_theater, format = "json")

        res = self.client.delete(f'/kinema/movie_theaters/{movie_theater.data["id"]}/')

        self.assertEqual(res.status_code, 204)