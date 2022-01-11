from django.db import models

# Create your models here.

class User(models.Model):
    account = models.CharField(primary_key=True,max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10)
    birthday = models.DateField()
    gender = models.BooleanField()
