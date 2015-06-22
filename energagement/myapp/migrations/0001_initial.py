# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buffer',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('description', models.TextField()),
                ('refresh_rate', models.FloatField()),
                ('created', models.DateField()),
                ('updated', models.DateField()),
                ('state', models.BooleanField(default=True)),
                ('label', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('category', models.CharField(max_length=200)),
                ('code', models.IntegerField(default=0)),
                ('longitude', models.FloatField(default=0.0)),
                ('latitude', models.FloatField(default=0.0)),
                ('surface', models.FloatField(default=0.0)),
                ('floors', models.IntegerField(default=1)),
                ('volume', models.FloatField(default=0.0)),
                ('kWh', models.FloatField(default=0.0)),
                ('kWh_m2', models.IntegerField(default=0.0)),
                ('kW', models.FloatField(default=0.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Counter',
            fields=[
                ('buffer_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, to='myapp.Buffer', primary_key=True)),
            ],
            options={
            },
            bases=('myapp.buffer',),
        ),
        migrations.CreateModel(
            name='ElectricVehicle',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('code', models.IntegerField(default=0)),
                ('municipality', models.CharField(max_length=200)),
                ('streets', models.CharField(max_length=200)),
                ('postcode', models.IntegerField(default=0)),
                ('longitude', models.IntegerField(default=1)),
                ('latitude', models.IntegerField(default=1)),
                ('map_area', models.IntegerField(default=0)),
                ('power', models.FloatField(default=0.0)),
                ('type', models.CharField(max_length=200)),
                ('kWh', models.FloatField(default=0.0)),
                ('kWh_user', models.FloatField(default=0.0)),
                ('total_charging_points', models.IntegerField(default=0)),
                ('available_charging_points', models.IntegerField(default=0)),
                ('tn', models.FloatField(default=0.0)),
                ('tn_kWh_user', models.FloatField(default=0.0)),
                ('euro_user', models.FloatField(default=0.0)),
                ('monthly_expenses', models.FloatField(default=0.0)),
                ('forecast_expenses', models.FloatField(default=0.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plug',
            fields=[
                ('buffer_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, to='myapp.Buffer', primary_key=True)),
            ],
            options={
            },
            bases=('myapp.buffer',),
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('buffer_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, to='myapp.Buffer', primary_key=True)),
            ],
            options={
            },
            bases=('myapp.buffer',),
        ),
        migrations.CreateModel(
            name='StreetLighting',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('metric', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='sensor',
            name='values',
            field=models.ManyToManyField(blank=True, to='myapp.Value', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='counter',
            name='ampere',
            field=models.OneToOneField(to='myapp.Value', related_name='7'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='counter',
            name='kwatt',
            field=models.OneToOneField(to='myapp.Value', related_name='1'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='counter',
            name='kwh1',
            field=models.OneToOneField(to='myapp.Value', related_name='2'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='counter',
            name='kwh2',
            field=models.OneToOneField(to='myapp.Value', related_name='3'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='counter',
            name='kwh3',
            field=models.OneToOneField(to='myapp.Value', related_name='4'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='counter',
            name='kwhtotal',
            field=models.OneToOneField(to='myapp.Value', related_name='5'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='counter',
            name='pf',
            field=models.OneToOneField(to='myapp.Value', related_name='8'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='counter',
            name='voltage',
            field=models.OneToOneField(to='myapp.Value', related_name='6'),
            preserve_default=True,
        ),
    ]
