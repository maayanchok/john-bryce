from django.db import models
from models import model
# Create your models here.

class User(models.Model):
  name = models.CharField(max_lenght = 50, default = None)
  birthdate = models.Date()
  email = models.EmailField()
  gender = models.CharField(max_lenght = 124, default = None)
  bio = models.CharField(max_lenght = 124, default = None)
  
  
  
  
  
