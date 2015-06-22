from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Value(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    metric = models.TextField()

class Buffer(models.Model):
    description = models.TextField()
    refresh_rate = models.FloatField()
    created = models.DateField()
    updated = models.DateField()
    state = models.BooleanField(default=True)
    label = models.TextField()

class Plug(Buffer):
    # Prizes mono On/Off
    pass

class Sensor(Buffer):
    # analink + digital for movement sensor
    values = models.ManyToManyField(Value, null=True, blank=True)

class Counter(Buffer):
    #
    kwatt = models.OneToOneField(Value,related_name="1")
    kwh1 = models.OneToOneField(Value,related_name="2")
    kwh2 = models.OneToOneField(Value,related_name="3")
    kwh3 = models.OneToOneField(Value,related_name="4")
    kwhtotal = models.OneToOneField(Value,related_name="5")
    voltage = models.OneToOneField(Value,related_name="6")
    ampere = models.OneToOneField(Value,related_name="7")
    pf = models.OneToOneField(Value,related_name="8")




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



class ElectricVehicle(models.Model):
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


class StreetLighting(models.Model):
    code = models.IntegerField(default=0)
    municipality = models.CharField(max_length=200, default="Athens")

