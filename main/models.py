from django.db import models


# Create your models here.
class Index(models.Model):
    publish = models.TimeField()
    last_value = models.FloatField()
    change = models.FloatField()
    percentage = models.FloatField()
    max = models.FloatField()
    min = models.FloatField()
    name = models.TextField()


class IndexInfluence(models.Model):
    symbol = models.TextField()
    name = models.TextField()
    final_price = models.FloatField()
    influence = models.FloatField()


class PopularIndex(models.Model):
    symbol = models.TextField()
    name = models.TextField()
    yesterday_price = models.FloatField()
    final_price = models.FloatField()
    max_price = models.FloatField()
    min_price = models.FloatField()
    count = models.BigIntegerField()
    volume = models.FloatField()
    value = models.FloatField()
    final_deal = models.FloatField()

