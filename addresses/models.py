import uuid
from django.db import models

class Address(models.Model):
    id = models.UUIDField(
            primary_key = True, 
            default = uuid.uuid4,
            editable = False
         )
    street = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    number = models.IntegerField()
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=8)