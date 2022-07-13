from django.db import models
import uuid

class Cinema(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50, unique=True)
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=30, null=True)
    opening_hours = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    address = models.ForeignKey("addresses.Address", on_delete=models.CASCADE, related_name="cinemas")
    user = models.ManyToManyField("users.User", related_name="cinemas", null=True) 
