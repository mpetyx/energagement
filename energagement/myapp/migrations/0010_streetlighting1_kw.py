# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_auto_20150711_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='streetlighting1',
            name='kw',
            field=models.ManyToManyField(related_name='kw', null=True, blank=True, to='myapp.Value'),
            preserve_default=True,
        ),
    ]
