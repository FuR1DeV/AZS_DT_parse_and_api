from django.db import models


class Azs(models.Model):
    """Модель таблицы куда мы будем записывать необходимые данные"""
    latitude = models.FloatField(null=False)
    longitude = models.FloatField(null=False)
    dt = models.CharField(max_length=150, null=True)
    dt_taneko = models.CharField(max_length=150, null=True)
    dt_winter = models.CharField(max_length=150, null=True)
    dt_arctic = models.CharField(max_length=150, null=True)
