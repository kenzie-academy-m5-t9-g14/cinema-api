from django.db import models
import uuid

class Seat(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    row = models.CharField(max_length=20)
    seat = models.CharField(max_length=20)
    availability  = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # movie_theater_id = models.ForeignKey("movie_theaters.MovieTheater", on_delete=models.CASCADE, related_name="seats")
