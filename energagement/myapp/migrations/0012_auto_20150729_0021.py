# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_auto_20150712_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buildingcounter',
            name='ape_kwh',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='buffer_ptr',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='co2_lt_m2',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='co2_tn',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='co2_tn_m2',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='cosf',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='euro_forecast',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='euro_m2_electricity',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='euro_m2_liquidfuel',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='euro_m2_monthly',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='kw',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='kwh',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='kwh_m2',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='kwh_m2_cooling',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='kwh_m2_heating',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='kwh_m2_lighting',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='kwh_m2_usagehours',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='kwh_m2_user',
        ),
        migrations.RemoveField(
            model_name='buildingcounter',
            name='lt_m2',
        ),
        migrations.DeleteModel(
            name='BuildingCounter',
        ),
        migrations.RemoveField(
            model_name='electricvehiclecounter',
            name='available_charging_points',
        ),
        migrations.RemoveField(
            model_name='electricvehiclecounter',
            name='buffer_ptr',
        ),
        migrations.RemoveField(
            model_name='electricvehiclecounter',
            name='co2_tn',
        ),
        migrations.RemoveField(
            model_name='electricvehiclecounter',
            name='co2_tn_user',
        ),
        migrations.RemoveField(
            model_name='electricvehiclecounter',
            name='euro_forecast',
        ),
        migrations.RemoveField(
            model_name='electricvehiclecounter',
            name='euro_m2_monthly',
        ),
        migrations.RemoveField(
            model_name='electricvehiclecounter',
            name='euro_user',
        ),
        migrations.RemoveField(
            model_name='electricvehiclecounter',
            name='kwh',
        ),
        migrations.RemoveField(
            model_name='electricvehiclecounter',
            name='kwh_user',
        ),
        migrations.RemoveField(
            model_name='electricvehiclecounter',
            name='total_charging_points',
        ),
        migrations.DeleteModel(
            name='ElectricVehicleCounter',
        ),
        migrations.RemoveField(
            model_name='streetlightingcounter',
            name='ape_kwh',
        ),
        migrations.RemoveField(
            model_name='streetlightingcounter',
            name='buffer_ptr',
        ),
        migrations.RemoveField(
            model_name='streetlightingcounter',
            name='co2_lt_m2',
        ),
        migrations.RemoveField(
            model_name='streetlightingcounter',
            name='co2_tn',
        ),
        migrations.RemoveField(
            model_name='streetlightingcounter',
            name='co2_tn_km',
        ),
        migrations.RemoveField(
            model_name='streetlightingcounter',
            name='cosf',
        ),
        migrations.RemoveField(
            model_name='streetlightingcounter',
            name='euro_forecast',
        ),
        migrations.RemoveField(
            model_name='streetlightingcounter',
            name='euro_line',
        ),
        migrations.RemoveField(
            model_name='streetlightingcounter',
            name='euro_monthly',
        ),
        migrations.RemoveField(
            model_name='streetlightingcounter',
            name='kw',
        ),
        migrations.RemoveField(
            model_name='streetlightingcounter',
            name='kwh',
        ),
        migrations.RemoveField(
            model_name='streetlightingcounter',
            name='kwh_km',
        ),
        migrations.RemoveField(
            model_name='streetlightingcounter',
            name='kwh_light',
        ),
        migrations.RemoveField(
            model_name='streetlightingcounter',
            name='kwh_line',
        ),
        migrations.RemoveField(
            model_name='streetlightingcounter',
            name='operating_lights_percentage',
        ),
        migrations.DeleteModel(
            name='StreetLightingCounter',
        ),
        migrations.AddField(
            model_name='building',
            name='ape_kwh',
            field=models.ManyToManyField(to='myapp.Value', related_name='ape_kwh_b', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='co2_lt_m2',
            field=models.ManyToManyField(to='myapp.Value', related_name='co2_lt_m2_b', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='co2_tn',
            field=models.ManyToManyField(to='myapp.Value', related_name='co2_tn_b', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='co2_tn_m2',
            field=models.ManyToManyField(to='myapp.Value', related_name='co2_tn_m2', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='cosf',
            field=models.ManyToManyField(to='myapp.Value', related_name='cosf_b', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='euro_forecast',
            field=models.ManyToManyField(to='myapp.Value', related_name='euro_forecast_b', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='euro_m2_electricity',
            field=models.ManyToManyField(to='myapp.Value', related_name='euro_m2_electricity', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='euro_m2_liquidfuel',
            field=models.ManyToManyField(to='myapp.Value', related_name='euro_m2_liquidfuel', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='euro_m2_monthly',
            field=models.ManyToManyField(to='myapp.Value', related_name='euro_m2_monthly', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='kw',
            field=models.ManyToManyField(to='myapp.Value', related_name='kw_b', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='kwh',
            field=models.ManyToManyField(to='myapp.Value', related_name='kwh_b', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='kwh_m2',
            field=models.ManyToManyField(to='myapp.Value', related_name='kwh_m2', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='kwh_m2_cooling',
            field=models.ManyToManyField(to='myapp.Value', related_name='kwh_m2_cooling', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='kwh_m2_heating',
            field=models.ManyToManyField(to='myapp.Value', related_name='kwh_m2_heating', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='kwh_m2_lighting',
            field=models.ManyToManyField(to='myapp.Value', related_name='kwh_m2_lighting', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='kwh_m2_usagehours',
            field=models.ManyToManyField(to='myapp.Value', related_name='kwh_m2_usagehours', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='kwh_m2_user',
            field=models.ManyToManyField(to='myapp.Value', related_name='kwh_m2_user', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='lt_m2',
            field=models.ManyToManyField(to='myapp.Value', related_name='lt_m2', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='electricvehicle',
            name='available_charging_points',
            field=models.ManyToManyField(to='myapp.Value', related_name='available_charging_points', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='electricvehicle',
            name='co2_tn',
            field=models.ManyToManyField(to='myapp.Value', related_name='co2_tn_e', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='electricvehicle',
            name='co2_tn_user',
            field=models.ManyToManyField(to='myapp.Value', related_name='co2_tn_user', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='electricvehicle',
            name='euro_forecast',
            field=models.ManyToManyField(to='myapp.Value', related_name='euro_forecast_e', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='electricvehicle',
            name='euro_m2_monthly',
            field=models.ManyToManyField(to='myapp.Value', related_name='euro_forecast', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='electricvehicle',
            name='euro_user',
            field=models.ManyToManyField(to='myapp.Value', related_name='euro_user', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='electricvehicle',
            name='kwh',
            field=models.ManyToManyField(to='myapp.Value', related_name='kwh_e', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='electricvehicle',
            name='kwh_user',
            field=models.ManyToManyField(to='myapp.Value', related_name='kwh_user', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='electricvehicle',
            name='total_charging_points',
            field=models.ManyToManyField(to='myapp.Value', related_name='total_charging_points', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='streetlighting',
            name='ape_kwh',
            field=models.ManyToManyField(to='myapp.Value', related_name='ape_kwh_s', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='streetlighting',
            name='co2_lt_m2',
            field=models.ManyToManyField(to='myapp.Value', related_name='co2_lt_m2_s', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='streetlighting',
            name='co2_tn',
            field=models.ManyToManyField(to='myapp.Value', related_name='co2_tn_s', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='streetlighting',
            name='co2_tn_km',
            field=models.ManyToManyField(to='myapp.Value', related_name='co2_tn_km', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='streetlighting',
            name='cosf',
            field=models.ManyToManyField(to='myapp.Value', related_name='cosf_s', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='streetlighting',
            name='euro_forecast',
            field=models.ManyToManyField(to='myapp.Value', related_name='euro_forecast_s', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='streetlighting',
            name='euro_line',
            field=models.ManyToManyField(to='myapp.Value', related_name='euro_line', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='streetlighting',
            name='euro_monthly',
            field=models.ManyToManyField(to='myapp.Value', related_name='euro_monthly', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='streetlighting',
            name='kw',
            field=models.ManyToManyField(to='myapp.Value', related_name='kw_s', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='streetlighting',
            name='kwh',
            field=models.ManyToManyField(to='myapp.Value', related_name='kwh_s', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='streetlighting',
            name='kwh_km',
            field=models.ManyToManyField(to='myapp.Value', related_name='kwh_km', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='streetlighting',
            name='kwh_light',
            field=models.ManyToManyField(to='myapp.Value', related_name='kwh_light', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='streetlighting',
            name='kwh_line',
            field=models.ManyToManyField(to='myapp.Value', related_name='kwh_line', blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='streetlighting',
            name='operatinglights_percentage',
            field=models.ManyToManyField(to='myapp.Value', related_name='operatinglights_percentage', blank=True, null=True),
            preserve_default=True,
        ),
    ]
