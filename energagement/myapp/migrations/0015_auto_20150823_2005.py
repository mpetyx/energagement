# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_auto_20150823_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plug',
            name='buffer_ptr',
        ),
        migrations.DeleteModel(
            name='Plug',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='buffer_ptr',
        ),
        migrations.DeleteModel(
            name='Buffer',
        ),
        migrations.RemoveField(
            model_name='sensor',
            name='values',
        ),
        migrations.DeleteModel(
            name='Sensor',
        ),
    ]
