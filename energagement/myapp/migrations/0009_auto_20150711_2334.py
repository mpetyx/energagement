# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20150701_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='timestamp',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
