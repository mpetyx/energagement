# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20150624_1004'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StreetLighting',
            new_name='StreetLighting1',
        ),
        migrations.AlterField(
            model_name='value',
            name='timestamp',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
