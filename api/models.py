from django.db import models

class Cars(models.Model):
    brand = models.CharField(max_length=32),
    model = models.CharField(max_length=32),
    year = models.BooleanField(default = False),
    car_mileage = models.CharField(max_length=32),
    horse_power = models.CharField(max_length=32),
    description = models.TextField(max_length=256),

