# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0026_auto_20151130_1653'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='beautician',
            name='Services',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='services',
        ),
        migrations.RemoveField(
            model_name='order',
            name='services',
        ),
    ]
