from django.db import models
import uuid

class Ticket(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    is_student = models.BooleanField(default=False)
    total_value = models.DecimalField(max_digits=8, decimal_places=2)
    status_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    movie_session = models.ForeignKey(
        "movie_sessions.MovieSession", on_delete=models.DO_NOTHING, related_name="tickets"
    )
    buyer = models.ForeignKey(
        "users.User", on_delete=models.DO_NOTHING, related_name="tickets"
    )
    payment_type = models.ForeignKey(
         "payment_types.PaymentType", on_delete=models.DO_NOTHING, related_name="tickets"
     ) 
    seats = models.ManyToManyField(
         "seats.Seat", related_name="tickets"
     ) 


    def __str__(self):
       return f'{self.id},{self.status_active}' 






