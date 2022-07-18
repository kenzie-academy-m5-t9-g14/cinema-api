
from cgitb import reset
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
import ipdb

from users.models import User


class MoviesViewTest(APITestCase):

    @classmethod
    def setUpTestData(cls) -> None:

        cls.superuser = User.objects.create_superuser(**{"name": "Gabriel", "password": "1234","email":"gabriel@admin.com","birth_date":"2022-02-02"})

        cls.token = Token.objects.create(user = cls.superuser)


        cls.movie = {
                        "name":"Senhor dos Aneis",
	                    "duration":"250m",
	                    "parental_rating":"14",
                        "sinopse":"um velho barbudo e sua turminhda do barulho",
                        "imdb_rating":"7.9",
                        "release_date":"2022-01-12",
                        "closing_date":"2022-03-12",
                        "genres" : [{"name":"ficção"}, {"name": "aventura"}]
                    }
 

    def test_creation_of_a_movie(self):

        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

        user_is_super = self.token.user.is_superuser 
        if user_is_super:
            res = self.client.post("/kinema/movies/", data = self.movie, format = "json")


        self.assertEqual(res.status_code, 201)
        self.assertTrue(user_is_super)


    def test_list_all_movies(self):
        res = self.client.get("/kinema/movies/")
        self.assertEqual(res.status_code, 200)
    
