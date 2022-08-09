from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from ipware import get_client_ip

# Create your models here.
  
class Dogs(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default=None)
    gender = models.CharField(max_length=124, default=None)
    race = models.CharField(max_length=124, default=None)


    def __str__(self):
        return self.name

#class Friends(models.Model):
    #pass

    

class Permissions(models.Model):
    location = models.BooleanField()
    camera = models.BooleanField()
    is_private = models.BooleanField()
    notifications = models.BooleanField()

    #owner = models.ForeignKey("User", on_delete=models.CASCADE)

