# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20150729_0021'),
    ]

    operations = [
        migrations.AddField(
            model_name='streetlighting1',
            name='latitude',
            field=models.IntegerField(default=23),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='streetlighting1',
            name='longitude',
            field=models.IntegerField(default=38),
            preserve_default=True,
        ),
    ]
