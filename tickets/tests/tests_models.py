from django.test import TestCase
from django.db import models
from cinemas.models import Cinema
from movie_sessions.models import MovieSession
from movie_theaters.models import MovieTheater
from movies.models import MoviesModel
from payment_types.models import PaymentType
from seats.models import Seat
from tickets.models import Ticket
from users.models import User
from addresses.models import Address
import uuid

class TicketsModelTest(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        cls.payment_type_data  = {"type":"credito"}
        cls.total_value_data   = 35.00
        cls.seats_data = [{"row":"A", "seat":"1"},{"row":"A", "seat":"2"}]
        cls.status_active_data = True       
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

        cls.ticketTeste = Ticket.objects.create(
            payment_type=cls.payment_type, 
            total_value=cls.total_value_data,
            movie_session = cls.session,
            buyer_id = cls.superuser.id
        )
        cls.ticketTeste.seats.set(cls.seat_array)

    
    def test_ticket_has_information_fields(self):             
        self.assertEqual(self.ticketTeste.payment_type, self.payment_type)
        self.assertEqual(self.ticketTeste.total_value, self.total_value_data)
        self.assertIsNotNone(self.ticketTeste.movie_session)  
        self.assertIsNotNone(self.ticketTeste.seats)

    def test_total_value(self):
        uuid = self.ticketTeste.id
        new_ticket = Ticket.objects.get(id=uuid)
        total_value_ticket = new_ticket._meta.get_field("total_value")
        self.assertIsNotNone(total_value_ticket)

    def test_object_name_is_id_comma_last_name(self):
        uuid = self.ticketTeste.id
        new_ticket = Ticket.objects.get(id= uuid)
        expected_object_name = f'{str(uuid)},{self.status_active_data}'  
        self.assertEquals(expected_object_name, str(new_ticket))

    def test_movie_theater_id_in_ticket(self):
        uuid = self.session.id
        self.assertEqual(uuid, self.ticketTeste.movie_session.id) 
