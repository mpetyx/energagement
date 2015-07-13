# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20150629_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='timestamp',
            field=models.DateField(),
            preserve_default=True,
        ),
    ]
