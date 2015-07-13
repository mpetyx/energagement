# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_streetlighting1_kw'),
    ]

    operations = [
        migrations.AddField(
            model_name='streetlighting1',
            name='kwh',
            field=models.ManyToManyField(blank=True, related_name='kwh', null=True, to='myapp.Value'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='streetlighting1',
            name='kwh_line',
            field=models.ManyToManyField(blank=True, related_name='kw_line', null=True, to='myapp.Value'),
            preserve_default=True,
        ),
    ]
