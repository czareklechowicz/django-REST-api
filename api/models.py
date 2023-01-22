from django.db import models

class Cars(models.Model):
    brand = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    price = models.CharField(max_length=32)
    year = models.TextField(max_length=32)
    kilometers = models.TextField(max_length=32)
    horse_power = models.TextField(max_length=32)
    description = models.TextField(max_length=256)

    
