import uuid
from django.db import models
from django.utils import timezone

class MovieSession(models.Model):
    id = models.UUIDField(
            primary_key = True, 
            default = uuid.uuid4,
            editable = False
         )
    exhibit_type = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    movie = models.ForeignKey("movies.MoviesModel", on_delete=models.CASCADE, related_name="movie_sessions")
    
    seat = models.ManyToManyField("seats.Seat", related_name="movie_sessions")
    # schedule = models.ManyToManyField("schedules.Schedule", related_name="sessions")