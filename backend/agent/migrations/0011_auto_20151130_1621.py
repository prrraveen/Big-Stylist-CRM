# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0010_auto_20151130_1616'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='duration',
        ),
        migrations.AddField(
            model_name='service',
            name='duration_in_min',
            field=models.IntegerField(default=0),
        ),
    ]
