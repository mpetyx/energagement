# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20150622_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='streetlighting',
            name='values',
            field=models.ManyToManyField(null=True, to='myapp.Value', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='streetlighting',
            name='municipality',
            field=models.CharField(default='Athens', max_length=200),
            preserve_default=True,
        ),
    ]
