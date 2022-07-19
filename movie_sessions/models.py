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
    status_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    movie = models.ForeignKey("movies.MoviesModel", on_delete=models.CASCADE, related_name="movie_sessions")
    movie_theater = models.ForeignKey("movie_theaters.MovieTheater", on_delete=models.CASCADE, related_name="movie_sessions")
    schedule = models.ManyToManyField("schedules.Schedule", related_name="sessions")
