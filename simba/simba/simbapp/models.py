from django.db import models
from django.db.models import Model

# Create your models here.

class Users(models.Model):
    username = models.CharField(max_length=50, default=None)
    firstname = models.CharField(max_length=50, default=None)
    lastname = models.CharField(max_length=50, default=None)
    email = models.EmailField()
    password = models.CharField(max_length=16, default=None)
    gender = models.CharField(max_length=124, default=None)
    description = models.CharField(max_length=124, default=None)
    #profile_pic
    #qr_code

    def __str__(self):
        return self.name

  
class Dogs(models.Model):
    name = models.CharField(max_length=50, default=None)
    birthdate = models.DateField()
    gender = models.CharField(max_length=124, default=None)
    race = models.CharField(max_length=124, default=None)

    #owner = models.ForeignKey("User", on_delete=models.CASCADE)

class Permissions(models.Model):
    location = models.BooleanField()
    camera = models.BooleanField()
    is_private = models.BooleanField()
    notifications = models.BooleanField()

    #owner = models.ForeignKey("User", on_delete=models.CASCADE)

