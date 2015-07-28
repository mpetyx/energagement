from django.db import models
# from django.contrib.auth.models import User

# Create your models here.

class Value(models.Model):
    timestamp = models.DateTimeField()
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

class Building(models.Model):
    category = models.CharField(max_length=200)
    building_code = models.IntegerField(default=0)
    municipality = models.CharField(max_length=200, default="Athens")
    street = models.CharField(max_length=200, default="Poseidonos")
    postcode = models.IntegerField(default=0)
    longitude = models.FloatField(default=0.0)
    latitude = models.FloatField(default=0.0)
    surface = models.FloatField(default=0.0)
    floors = models.IntegerField(default=1)
    volume = models.FloatField(default=0.0)

    kwh=models.ManyToManyField(Value, null=True, blank=True, related_name="kwh_b")
    kwh_m2=models.ManyToManyField(Value, null=True, blank=True, related_name="kwh_m2")
    kwh_m2_lighting=models.ManyToManyField(Value, null=True, blank=True, related_name="kwh_m2_lighting")
    kwh_m2_cooling=models.ManyToManyField(Value, null=True, blank=True, related_name="kwh_m2_cooling")
    kwh_m2_heating=models.ManyToManyField(Value, null=True, blank=True, related_name="kwh_m2_heating")
    lt_m2=models.ManyToManyField(Value, null=True, blank=True, related_name="lt_m2")
    kwh_m2_user=models.ManyToManyField(Value, null=True, blank=True, related_name="kwh_m2_user")
    kwh_m2_usagehours=models.ManyToManyField(Value, null=True, blank=True, related_name="kwh_m2_usagehours")
    kw=models.ManyToManyField(Value, null=True, blank=True, related_name="kw_b")
    cosf=models.ManyToManyField(Value, null=True, blank=True, related_name="cosf_b")
    co2_tn=models.ManyToManyField(Value, null=True, blank=True, related_name="co2_tn_b")
    co2_tn_m2=models.ManyToManyField(Value, null=True, blank=True, related_name="co2_tn_m2")
    co2_lt_m2=models.ManyToManyField(Value, null=True, blank=True, related_name="co2_lt_m2_b")
    ape_kwh=models.ManyToManyField(Value, null=True, blank=True, related_name="ape_kwh_b")
    euro_m2_electricity=models.ManyToManyField(Value, null=True, blank=True, related_name="euro_m2_electricity")
    euro_m2_liquidfuel=models.ManyToManyField(Value, null=True, blank=True, related_name="euro_m2_liquidfuel")
    euro_m2_monthly=models.ManyToManyField(Value, null=True, blank=True, related_name="euro_m2_monthly")
    euro_forecast=models.ManyToManyField(Value, null=True, blank=True, related_name="euro_forecast_b")


class StreetLighting(models.Model):
    line_code = models.IntegerField(default=0)
    municipality = models.CharField(max_length=200, default="Athens")
    streets = models.CharField(max_length=200, default="Poseidonos")
    postcode = models.IntegerField(default=0)
    longitude = models.IntegerField(default=1)
    latitude = models.IntegerField(default=1)
    map_area = models.IntegerField(default=0)
    power_installed = models.FloatField(default=0.0)
    line_length = models.FloatField(default=0.0)
    lights_number = models.IntegerField(default=0)

    kwh=models.ManyToManyField(Value, null=True, blank=True, related_name="kwh_s")
    kwh_line=models.ManyToManyField(Value, null=True, blank=True, related_name="kwh_line")
    kwh_light=models.ManyToManyField(Value, null=True, blank=True, related_name="kwh_light")
    kwh_km=models.ManyToManyField(Value, null=True, blank=True, related_name="kwh_km")
    kw=models.ManyToManyField(Value, null=True, blank=True, related_name="kw_s")
    cosf=models.ManyToManyField(Value, null=True, blank=True, related_name="cosf_s")
    operatinglights_percentage=models.ManyToManyField(Value, null=True, blank=True, related_name="operatinglights_percentage")
    co2_tn=models.ManyToManyField(Value, null=True, blank=True, related_name="co2_tn_s")
    co2_tn_km=models.ManyToManyField(Value, null=True, blank=True, related_name="co2_tn_km")
    co2_lt_m2=models.ManyToManyField(Value, null=True, blank=True, related_name="co2_lt_m2_s")
    ape_kwh=models.ManyToManyField(Value, null=True, blank=True, related_name="ape_kwh_s")
    euro_line=models.ManyToManyField(Value, null=True, blank=True, related_name="euro_line")
    euro_monthly=models.ManyToManyField(Value, null=True, blank=True, related_name="euro_monthly")
    euro_forecast=models.ManyToManyField(Value, null=True, blank=True, related_name="euro_forecast_s")


class ElectricVehicle(models.Model):
    chargingpoint_code = models.IntegerField(default=0)
    municipality = models.CharField(max_length=200, default="Athens")
    streets = models.CharField(max_length=200, default="Poseidonos")
    postcode = models.IntegerField(default=0)
    longitude = models.IntegerField(default=1)
    latitude = models.IntegerField(default=1)
    map_area = models.IntegerField(default=0)
    power = models.FloatField(default=0.0)
    type = models.CharField(max_length=200)

    kwh=models.ManyToManyField(Value, null=True, blank=True, related_name="kwh_e")
    kwh_user=models.ManyToManyField(Value, null=True, blank=True, related_name="kwh_user")
    total_charging_points=models.ManyToManyField(Value, null=True, blank=True, related_name="total_charging_points")
    available_charging_points=models.ManyToManyField(Value, null=True, blank=True, related_name="available_charging_points")
    co2_tn=models.ManyToManyField(Value, null=True, blank=True, related_name="co2_tn_e")
    co2_tn_user=models.ManyToManyField(Value, null=True, blank=True, related_name="co2_tn_user")
    euro_user=models.ManyToManyField(Value, null=True, blank=True, related_name="euro_user")
    euro_m2_monthly=models.ManyToManyField(Value, null=True, blank=True, related_name="euro_forecast")
    euro_forecast=models.ManyToManyField(Value, null=True, blank=True, related_name="euro_forecast_e")


class StreetLighting1(models.Model):
    values=models.ManyToManyField(Value, null=True, blank=True)
    kwh=models.ManyToManyField(Value, null=True, blank=True, related_name="kwh")
    kwh_line=models.ManyToManyField(Value, null=True, blank=True, related_name="kw_line")
    kw=models.ManyToManyField(Value, null=True, blank=True, related_name="kw")
    code = models.IntegerField(default=0)
    municipality = models.CharField(max_length=200, default="Athens")

