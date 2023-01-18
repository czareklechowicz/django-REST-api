from django.db import models

class Cars(models.Model):
    brand = models.CharField(max_length=32),
    model = models.TextField(max_length=32),
    year = models.BooleanField(default = False),
    kilometers = models.TextField(max_length=32),
    horse_power = models.TextField(max_length=32),
    description = models.TextField(max_length=256),

