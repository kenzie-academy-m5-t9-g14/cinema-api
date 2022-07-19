import json
from rest_framework.test import APITestCase
from cinemas.models import Cinema
from users.models import User
from addresses.models import Address
from rest_framework.authtoken.models import Token
import ipdb

class CinemaViewsTest(APITestCase):
	@classmethod
	def setUpTestData(cls) -> None:
		cls.address = {
			"street":"Avenida Brazil",
		    "district": "Center",
		    "number": 84,
		    "zipcode":"85802120",
		    "city":"cascavel"
		}

		cls.cinema = {
			"name":"Cinemax223",
			"phone": "555-8896",
			"address":{
				"street":"Avenida Brazil",
				"district": "Center",
				"number": 84,
				"zipcode":"85802120",
				"city":"cascavel"
			}
		}

		cls.phone = '523-2323'

		cls.address = Address.objects.create(**cls.address)

		cls.user = User.objects.create_superuser(**{"name": "owner_test", "password": "123","email":"owner@test.com","birth_date":"2012-12-12","address_id":cls.address.id})

		cls.token = Token.objects.create(user=cls.user)

		cls.cinemas = [Cinema.objects.create(
            name= f'cinema{cinema_id}',
            phone = '555-2323',
            address= cls.address,
        ) for cinema_id in range(10)]


	def test_create_cinema(self):
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
		response = self.client.post('/kinema/cinemas/', data=self.cinema, format='json')
		self.assertEqual(response.status_code, 201)


	def test_anyone_can_list_cinemas(self):
		response = self.client.get('/kinema/cinemas/')
		self.assertEqual(response.status_code, 200)

	
	def test_anyone_can_filter_product(self):
		response = self.client.get(f'/kinema/cinemas/{self.cinemas[0].id}/')
		self.assertEqual(response.status_code, 200)

	def test_update(self):
		self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
		response = self.client.patch(f'/kinema/cinemas/{self.cinemas[0].id}/', {'phone' : self.phone})
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.data['phone'], self.phone)