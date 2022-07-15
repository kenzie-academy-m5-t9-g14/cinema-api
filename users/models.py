import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from .utils import CustomUserManager


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50, null=False)
    cpf = models.CharField(max_length=11, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    birth_date = models.DateField(null=False)
    cellphone = models.CharField(max_length=13, null=True)
    genre = models.CharField(max_length=20, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    username = models.CharField(unique=False, null=True, max_length=255)

    address = models.ForeignKey('addresses.Address', on_delete=models.DO_NOTHING, related_name='users')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'cpf', 'birth_date',]
    objects = CustomUserManager()
    
