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

class BuildingCounter(Buffer):
    kwh = models.OneToOneField(Value,related_name="1")
    kwh_m2 = models.OneToOneField(Value,related_name="2")
    kwh_m2_lighting = models.OneToOneField(Value,related_name="3")
    kwh_m2_cooling = models.OneToOneField(Value,related_name="4")
    kwh_m2_heating = models.OneToOneField(Value,related_name="5")
    lt_m2 =  models.OneToOneField(Value,related_name="6")
    kwh_m2_user = models.OneToOneField(Value,related_name="7")
    kwh_m2_usagehours = models.OneToOneField(Value,related_name="8")
    kw = models.OneToOneField(Value,related_name="9")
    cosf = models.OneToOneField(Value,related_name="10")
    co2_tn = models.OneToOneField(Value,related_name="11")
    co2_tn_m2 = models.OneToOneField(Value,related_name="12")
    co2_lt_m2 = models.OneToOneField(Value,related_name="13")
    ape_kwh = models.OneToOneField(Value,related_name="14")
    euro_m2_electricity = models.OneToOneField(Value,related_name="15")
    euro_m2_liquidfuel = models.OneToOneField(Value,related_name="16")
    euro_m2_monthly = models.OneToOneField(Value,related_name="17")
    euro_forecast = models.OneToOneField(Value,related_name="18")

class StreetLightingCounter(Buffer):
    kwh = models.OneToOneField(Value,related_name="19")
    kwh_line = models.OneToOneField(Value,related_name="20")
    kwh_light = models.OneToOneField(Value,related_name="21")
    kwh_km = models.OneToOneField(Value,related_name="22")
    kw = models.OneToOneField(Value,related_name="23")
    cosf =  models.OneToOneField(Value,related_name="24")
    operating_lights_percentage = models.OneToOneField(Value,related_name="25")
    co2_tn = models.OneToOneField(Value,related_name="26")
    co2_tn_km = models.OneToOneField(Value,related_name="27")
    co2_lt_m2 = models.OneToOneField(Value,related_name="28")
    ape_kwh = models.OneToOneField(Value,related_name="29")
    euro_line = models.OneToOneField(Value,related_name="30")
    euro_monthly = models.OneToOneField(Value,related_name="31")
    euro_forecast = models.OneToOneField(Value,related_name="32")

class ElectricVehicleCounter(Buffer):
    kwh = models.OneToOneField(Value,related_name="33")
    kwh_user = models.OneToOneField(Value,related_name="34")
    total_charging_points = models.OneToOneField(Value,related_name="35")
    available_charging_points = models.OneToOneField(Value,related_name="36")
    co2_tn = models.OneToOneField(Value,related_name="37")
    co2_tn_user = models.OneToOneField(Value,related_name="38")
    euro_user = models.OneToOneField(Value,related_name="39")
    euro_m2_monthly = models.OneToOneField(Value,related_name="40")
    euro_forecast = models.OneToOneField(Value,related_name="41")

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

    #kwh = models.OneToOneField(Value, null=True, blank=True)
    # kwh_m2 = models.OneToOneField(Value, null=True, blank=True)
    #kwh_m2_lighting = models.OneToOneField(Value, null=True, blank=True)
    #kwh_m2_cooling = models.OneToOneField(Value, null=True, blank=True)
    #kwh_m2_heating = models.OneToOneField(Value, null=True, blank=True)
    #lt_m2 =  models.OneToOneField(Value, null=True, blank=True)
    #kwh_m2_user = models.OneToOneField(Value, null=True, blank=True)
    #kwh_m2_usagehours = models.OneToOneField(Value, null=True, blank=True)
    #kw = models.OneToOneField(Value, null=True, blank=True)
    #cosf = models.OneToOneField(Value, null=True, blank=True)
    #co2_tn = models.OneToOneField(Value, null=True, blank=True)
    #co2_tn_m2 = models.OneToOneField(Value, null=True, blank=True)
    #co2_lt_m2 = models.OneToOneField(Value, null=True, blank=True)
    #ape_kwh = models.OneToOneField(Value, null=True, blank=True)
    #euro_m2_electricity = models.OneToOneField(Value, null=True, blank=True)
    #euro_m2_liquidfuel = models.OneToOneField(Value, null=True, blank=True)
    #euro_m2_monthly = models.OneToOneField(Value, null=True, blank=True)
    #euro_forecast = models.OneToOneField(Value, null=True, blank=True)'''


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
    #kwh = models.OneToOneField(Value, null=True, blank=True)
    #kwh_line = models.OneToOneField(Value, null=True, blank=True)
    #kwh_light = models.OneToOneField(Value, null=True, blank=True)
    #kwh_km = models.OneToOneField(Value, null=True, blank=True)
    #kw = models.OneToOneField(Value, null=True, blank=True)
    #cosf =  models.OneToOneField(Value, null=True, blank=True)
    #operatinglights_percentage = models.OneToOneField(Value, null=True, blank=True)
    #co2_tn = models.OneToOneField(Value, null=True, blank=True)
    #co2_tn_km = models.OneToOneField(Value, null=True, blank=True)
    #co2_lt_m2 = models.OneToOneField(Value, null=True, blank=True)
    #ape_kwh = models.OneToOneField(Value, null=True, blank=True)
    #euro_line = models.OneToOneField(Value, null=True, blank=True)
    #euro_monthly = models.OneToOneField(Value, null=True, blank=True)
    #euro_forecast = models.OneToOneField(Value, null=True, blank=True)


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

    #kwh = models.OneToOneField(Value, null=True, blank=True)
    # kwh_user = models.OneToOneField(Value, null=True, blank=True)
    #total_charging_points = models.OneToOneField(Value, null=True, blank=True)
    #available_charging_points = models.OneToOneField(Value, null=True, blank=True)
    #co2_tn = models.OneToOneField(Value, null=True, blank=True)
    #co2_tn_user = models.OneToOneField(Value, null=True, blank=True)
    #euro_user = models.OneToOneField(Value, null=True, blank=True)
    #euro_m2_monthly = models.OneToOneField(Value, null=True, blank=True)
    #euro_forecast = models.OneToOneField(Value, null=True, blank=True) '''



class StreetLighting1(models.Model):
    values=models.ManyToManyField(Value, null=True, blank=True)
    kwh=models.ManyToManyField(Value, null=True, blank=True, related_name="kwh")
    kwh_line=models.ManyToManyField(Value, null=True, blank=True, related_name="kw_line")
    kw=models.ManyToManyField(Value, null=True, blank=True, related_name="kw")
    code = models.IntegerField(default=0)
    municipality = models.CharField(max_length=200, default="Athens")

