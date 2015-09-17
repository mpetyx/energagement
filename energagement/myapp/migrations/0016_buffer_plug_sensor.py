# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_auto_20150823_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buffer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Plug',
            fields=[
                ('buffer_ptr', models.OneToOneField(parent_link=True, to='myapp.Buffer', auto_created=True, primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=('myapp.buffer',),
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('buffer_ptr', models.OneToOneField(parent_link=True, to='myapp.Buffer', auto_created=True, primary_key=True, serialize=False)),
                ('values', models.ManyToManyField(blank=True, to='myapp.Value', null=True)),
            ],
            options={
            },
            bases=('myapp.buffer',),
        ),
    ]
