# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_buffer_plug_sensor'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('EVs', models.ManyToManyField(blank=True, to='myapp.ElectricVehicle', null=True, related_name='EVs')),
                ('buildings', models.ManyToManyField(blank=True, to='myapp.Building', null=True, related_name='buildings')),
                ('street_ligthing', models.ManyToManyField(blank=True, to='myapp.StreetLighting', null=True, related_name='street_lighting')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='value',
            name='metric',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]
