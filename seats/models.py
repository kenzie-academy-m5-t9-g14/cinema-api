from django.db import models
import uuid

class Seat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    row = models.CharField(max_length=20)
    seat = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ticket_seat_id = models.UUIDField(default=uuid.uuid4)
    movie_theater = models.ForeignKey("movie_theaters.MovieTheater", on_delete=models.DO_NOTHING, related_name="seats")


class SeatMap(models.Model):
    seatMap = models.ManyToManyField("seats.Seat",related_name="seatMap")