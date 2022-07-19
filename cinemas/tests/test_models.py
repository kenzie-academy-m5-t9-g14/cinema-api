from django.test import TestCase
import ipdb
from cinemas.models import Cinema
from addresses.models import Address
from users.models import User

class CinemaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        
        cls.phone = '555-2323'


        cls.cinema = {
	        "name":"Cinemax223",
	        "phone": "555-8896"
        }
	        
        cls.address = {
		        "street":"Avenida Brazil",
		        "district": "Center",
		        "number": 84,
		        "zipcode":"85802120",
		        "city":"cascavel"
	    }

        
        cls.address = Address.objects.create(**cls.address)


        cls.cinemas = [Cinema.objects.create(
            name= f'cinema{cinema_id}',
            phone = cls.phone,
            address= cls.address,
        ) for cinema_id in range(10)]
        
        cls.cinema_owner = User.objects.create_superuser(**{"name": "owner_test", "password": "123","email":"owner@test.com","birth_date":"2012-12-12","address_id":cls.address.id})

    
    def test_user_may_contain_multiple_cinemas(self):

        for cinema in self.cinemas:
            self.cinema_owner.cinemas.add(cinema) 
            self.cinema_owner.save()

        self.assertEquals(
                len(self.cinemas), 
                self.cinema_owner.cinemas.count()
            )
      
    
    
    def test_product_has_information_fields(self):

        for cinema in self.cinemas:
            
            self.assertEqual(cinema.phone, self.phone)
            self.assertEqual(cinema.address, self.address)
            self.assertTrue(cinema.name)