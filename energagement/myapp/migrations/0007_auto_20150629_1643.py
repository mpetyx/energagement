# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20150629_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildingcounter',
            name='ape_kwh',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='14'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildingcounter',
            name='co2_lt_m2',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='13'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildingcounter',
            name='co2_tn',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='11'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildingcounter',
            name='co2_tn_m2',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildingcounter',
            name='cosf',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='10'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildingcounter',
            name='euro_forecast',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='18'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildingcounter',
            name='euro_m2_electricity',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='15'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildingcounter',
            name='euro_m2_liquidfuel',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='16'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildingcounter',
            name='euro_m2_monthly',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='17'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildingcounter',
            name='kw',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='9'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildingcounter',
            name='kwh',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildingcounter',
            name='kwh_m2',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildingcounter',
            name='kwh_m2_cooling',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='4'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildingcounter',
            name='kwh_m2_heating',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='5'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildingcounter',
            name='kwh_m2_lighting',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='3'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildingcounter',
            name='kwh_m2_usagehours',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='8'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildingcounter',
            name='kwh_m2_user',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='7'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buildingcounter',
            name='lt_m2',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='6'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electricvehiclecounter',
            name='available_charging_points',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='36'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electricvehiclecounter',
            name='co2_tn',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='37'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electricvehiclecounter',
            name='co2_tn_user',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='38'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electricvehiclecounter',
            name='euro_forecast',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='41'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electricvehiclecounter',
            name='euro_m2_monthly',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='40'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electricvehiclecounter',
            name='euro_user',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='39'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electricvehiclecounter',
            name='kwh',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='33'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electricvehiclecounter',
            name='kwh_user',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='34'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='electricvehiclecounter',
            name='total_charging_points',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='35'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='streetlightingcounter',
            name='ape_kwh',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='29'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='streetlightingcounter',
            name='co2_lt_m2',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='28'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='streetlightingcounter',
            name='co2_tn',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='26'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='streetlightingcounter',
            name='co2_tn_km',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='27'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='streetlightingcounter',
            name='cosf',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='24'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='streetlightingcounter',
            name='euro_forecast',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='32'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='streetlightingcounter',
            name='euro_line',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='30'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='streetlightingcounter',
            name='euro_monthly',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='31'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='streetlightingcounter',
            name='kw',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='23'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='streetlightingcounter',
            name='kwh',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='19'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='streetlightingcounter',
            name='kwh_km',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='22'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='streetlightingcounter',
            name='kwh_light',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='21'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='streetlightingcounter',
            name='kwh_line',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='20'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='streetlightingcounter',
            name='operating_lights_percentage',
            field=models.OneToOneField(default=0, to='myapp.Value', related_name='25'),
            preserve_default=False,
        ),
    ]
