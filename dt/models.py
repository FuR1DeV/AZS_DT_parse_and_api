from django.db import models

# Create your models here.


class Azs(models.Model):
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    dt = models.CharField(max_length=150)
    dt_taneko = models.CharField(max_length=150)
    dt_winter = models.CharField(max_length=150)
    dt_arctic = models.CharField(max_length=150)
