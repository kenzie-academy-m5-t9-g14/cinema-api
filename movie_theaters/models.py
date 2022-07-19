from uuid import uuid4
from django.db import models

class MovieTheater(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=30)
    number_of_seats = models.IntegerField()
    exhibit_type = models.CharField(max_length=30)
    seats_id = models.UUIDField(default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    cinema = models.ForeignKey(
        "cinemas.Cinema", on_delete=models.CASCADE, related_name="movie_theathers"
    )
    