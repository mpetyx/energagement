# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20150629_1511'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingCounter',
            fields=[
                ('buffer_ptr', models.OneToOneField(serialize=False, primary_key=True, to='myapp.Buffer', auto_created=True, parent_link=True)),
            ],
            options={
            },
            bases=('myapp.buffer',),
        ),
        migrations.CreateModel(
            name='ElectricVehicleCounter',
            fields=[
                ('buffer_ptr', models.OneToOneField(serialize=False, primary_key=True, to='myapp.Buffer', auto_created=True, parent_link=True)),
            ],
            options={
            },
            bases=('myapp.buffer',),
        ),
        migrations.CreateModel(
            name='StreetLighting',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('line_code', models.IntegerField(default=0)),
                ('municipality', models.CharField(default='Athens', max_length=200)),
                ('streets', models.CharField(default='Poseidonos', max_length=200)),
                ('postcode', models.IntegerField(default=0)),
                ('longitude', models.IntegerField(default=1)),
                ('latitude', models.IntegerField(default=1)),
                ('map_area', models.IntegerField(default=0)),
                ('power_installed', models.FloatField(default=0.0)),
                ('line_length', models.FloatField(default=0.0)),
                ('lights_number', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StreetLightingCounter',
            fields=[
                ('buffer_ptr', models.OneToOneField(serialize=False, primary_key=True, to='myapp.Buffer', auto_created=True, parent_link=True)),
            ],
            options={
            },
            bases=('myapp.buffer',),
        ),
        migrations.RemoveField(
            model_name='counter',
            name='ampere',
        ),
        migrations.RemoveField(
            model_name='counter',
            name='buffer_ptr',
        ),
        migrations.RemoveField(
            model_name='counter',
            name='kwatt',
        ),
        migrations.RemoveField(
            model_name='counter',
            name='kwh1',
        ),
        migrations.RemoveField(
            model_name='counter',
            name='kwh2',
        ),
        migrations.RemoveField(
            model_name='counter',
            name='kwh3',
        ),
        migrations.RemoveField(
            model_name='counter',
            name='kwhtotal',
        ),
        migrations.RemoveField(
            model_name='counter',
            name='pf',
        ),
        migrations.RemoveField(
            model_name='counter',
            name='voltage',
        ),
        migrations.DeleteModel(
            name='Counter',
        ),
        migrations.RenameField(
            model_name='building',
            old_name='code',
            new_name='building_code',
        ),
        migrations.RenameField(
            model_name='building',
            old_name='kWh_m2',
            new_name='postcode',
        ),
        migrations.RenameField(
            model_name='electricvehicle',
            old_name='available_charging_points',
            new_name='chargingpoint_code',
        ),
        migrations.RemoveField(
            model_name='building',
            name='kW',
        ),
        migrations.RemoveField(
            model_name='building',
            name='kWh',
        ),
        migrations.RemoveField(
            model_name='electricvehicle',
            name='code',
        ),
        migrations.RemoveField(
            model_name='electricvehicle',
            name='euro_user',
        ),
        migrations.RemoveField(
            model_name='electricvehicle',
            name='forecast_expenses',
        ),
        migrations.RemoveField(
            model_name='electricvehicle',
            name='kWh',
        ),
        migrations.RemoveField(
            model_name='electricvehicle',
            name='kWh_user',
        ),
        migrations.RemoveField(
            model_name='electricvehicle',
            name='monthly_expenses',
        ),
        migrations.RemoveField(
            model_name='electricvehicle',
            name='tn',
        ),
        migrations.RemoveField(
            model_name='electricvehicle',
            name='tn_kWh_user',
        ),
        migrations.RemoveField(
            model_name='electricvehicle',
            name='total_charging_points',
        ),
        migrations.AddField(
            model_name='building',
            name='municipality',
            field=models.CharField(default='Athens', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='building',
            name='street',
            field=models.CharField(default='Poseidonos', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='electricvehicle',
            name='municipality',
            field=models.CharField(default='Athens', max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='electricvehicle',
            name='streets',
            field=models.CharField(default='Poseidonos', max_length=200),
            preserve_default=True,
        ),
    ]
