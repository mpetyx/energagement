# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20150624_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
