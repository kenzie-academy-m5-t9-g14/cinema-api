import uuid
from django.db import models
from django.utils import timezone

class Schedule(models.Model):
    id = models.UUIDField(
            primary_key = True, 
            default = uuid.uuid4,
            editable = False
         )
    hour = models.TimeField()
    date = models.DateField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)


    def __repr__(self) -> str:
        return f"Schedule {self.id} ({self.name})"