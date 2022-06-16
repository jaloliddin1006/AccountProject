from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True,blank=True)
    phone = models.CharField(null=True, max_length=20)
    address = models.CharField(null=True,max_length=100)


