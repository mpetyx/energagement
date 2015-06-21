from django.db import models

# Create your models here.

class Building(models.Model):
    category = models.CharField(max_length=200)
    code = models.IntegerField(default=0)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    surface = models.FloatField(default=0.0)
    floors = models.IntegerField(default=1)
    volume = models.FloatField(default=0.0)
    kWh = models.FloatField(default=0.0)
    kWh_m2 = models.IntegerField(default=0.0)
    kW = models.FloatField(default=0.0)



class Electric_Vehicle(models.Model):
    code = models.IntegerField(default=0)
    municipality = models.CharField(max_length=200)
    streets = models.CharField(max_length=200)
    postcode = models.IntegerField(default=0)
    longitude = models.IntegerField(default=1)
    latitude = models.IntegerField(default=1)
    map_area = models.IntegerField(default=0)
    power = models.FloatField(default=0.0)
    type = models.CharField(max_length=200)
    kWh = models.FloatField(default=0.0)
    kWh_user = models.FloatField(default=0.0)
    total_charging_points = models.IntegerField(default=0)
    available_charging_points = models.IntegerField(default=0)
    tn = models.FloatField(default=0.0)
    tn_kWh_user = models.FloatField(default=0.0)
    euro_user = models.FloatField(default=0.0)
    monthly_expenses = models.FloatField(default=0.0)
    forecast_expenses = models.FloatField(default=0.0)



class Choice(models.Model):

    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
