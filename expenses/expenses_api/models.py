from django.db import models

# Create your models here.

class Transaction(models.Model):
    name = models.CharField(default = '', max_length = 128)
    amount = models.IntegerField(default = 0)
    date = models.DateField()
    category = models.CharField(default = '', max_length = 128)

    def __str__(self):
        return self.name




