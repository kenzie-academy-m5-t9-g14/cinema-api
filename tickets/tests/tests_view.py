from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from addresses.models import Address
from cinemas.models import Cinema
from movie_sessions.models import MovieSession
from movie_theaters.models import MovieTheater
from movies.models import MoviesModel
from payment_types.models import PaymentType
from seats.models import Seat
from tickets.models import Ticket
from users.models import User
from rest_framework.views import status

class TicketsViewAndAutenticationTest(APITestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.first_name = "Camila"
        cls.last_name = "Suzuki"
        cls.email = "camila@gmail.com"
        cls.emailAdmin = "camilaAdmin@gmail.com"
        cls.password = "senha_forte"

        cls.address_user_data = {
                "street":"rua mockup",
                "district": "district",
                "number": 100,
                "zipcode":"1597536",
                "city":"bauru"
        }
        cls.address_user = Address.objects.create(**cls.address_user_data)
        cls.userTeste = User.objects.create_user(
            first_name=cls.first_name, 
            last_name=cls.last_name,
            email = cls.email,
            birth_date="2000-01-11",
            password = cls.password,
            address_id=cls.address_user.id
        )

        cls.userTesteAdmin = User.objects.create_superuser(
            first_name=cls.first_name, 
            last_name=cls.last_name,
            email = cls.emailAdmin,
            password = cls.password,
            birth_date="2000-01-11",
            address_id=cls.address_user.id

        ) 

        cls.tokenUser = Token.objects.create(user=cls.userTeste)
        cls.tokenAdmin = Token.objects.create(user=cls.userTesteAdmin)

        cls.payment_type_data  = {"type":"credito"}
        cls.total_value_data   = 35.00

        cls.status_active_data = True       


        cls.address_cinema_data = {
                "street":"rua exemplo",
                "district": "cine ma",
                "number": 49,
                "zipcode":"36555563",
                "city":"bauru"
        }

        
        cls.address_cinema = Address.objects.create(**cls.address_cinema_data)

        cls.superuser_data = {
            "name": "super user", 
            "password": "senha_forte",
            "email":"super@user.com",
            "birth_date":"2000-4-03",
            "address_id":cls.address_user.id
        }
        
        cls.superuser = User.objects.create_superuser(**cls.superuser_data)

        cls.cinema_data = {
              "name":"Daslu2",
              "phone":"434725566",
              "email":"daslu@gmail.com",
              "opening_hours": "10:00 - 21:00",
              "address":cls.address_cinema
        }

        cls.cinema = Cinema.objects.create(**cls.cinema_data)

        cls.movie_theaters_data = {
            "name":"Sala 2",
            "type":"3D",
            "number_of_seats":"60",
            "exhibit_type":"Legendado",
            "cinema_id" : cls.cinema.id
        }

        cls.movie_theaters = MovieTheater.objects.create(**cls.movie_theaters_data)

        cls.seat_data = {
             "row": "A",
             "seat": "2",
             "movie_theater": cls.movie_theaters
        }

        cls.seats_contain = [Seat.objects.create(
            row=f'Row {rangeNumber}',
            seat = f'Row {rangeNumber}',
            movie_theater = cls.movie_theaters
        ) for rangeNumber in range(1, 6)]

        cls.seat = Seat.objects.create(**cls.seat_data)
        cls.seat_array = [cls.seat]

        cls.movie_data = {
               "name":"Senhor dos Aneis",
               "duration": "250 min ",
               "parental_rating": "14",
               "sinopse":"Um velho barbudo e sua turminha do barulho",
               "imdb_rating": "7.9",
               "release_date":"2022-01-12",
               "closing_date": "2022-03-12",
        }

        cls.movie = MoviesModel.objects.create(**cls.movie_data)

        cls.session_data ={
            "exhibit_type":"legendado",  
            "price":35.00, 
            "movie":cls.movie,
            "movie_theater": cls.movie_theaters,
        }

        cls.session = MovieSession.objects.create(**cls.session_data)
       
        cls.payment_type = PaymentType.objects.create(**cls.payment_type_data)

        cls.ticketTesteMockup = Ticket.objects.create(
            payment_type=cls.payment_type, 
            total_value=cls.total_value_data,
            movie_session = cls.session,
            buyer_id = cls.superuser.id
        )
        cls.ticketTesteMockup.seats.set(cls.seat_array)


    def test_only_autenticated_can_create_ticket_fail(self):
        uuid = self.session.id
        self.ticketTeste = {
	        "payment_type": {
	        "type":"credito"},
	        "total_value": 35.00,
	        "seats":[
		       {"row":"A", "seat":"1"},
		       {"row":"A", "seat":"2"}],
            "session":self.session.id       
        }

        res = self.client.post(
            f"/kinema/movie_session/{uuid}/ticket/", data=self.ticketTeste,format = "json"
        )

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)  

    def test_user_can_list_all_tickets(self):
        uuid = self.ticketTesteMockup.id
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.tokenUser.key)
        response = self.client.get(f'/kinema/tickets/{uuid}/')
        self.assertEqual(response.status_code, 200)
      

       