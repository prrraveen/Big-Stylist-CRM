# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0057_auto_20151123_1840'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='lead_status',
            field=models.IntegerField(default=1, blank=True, choices=[(1, b'Converted'), (2, b'Canceled')]),
        ),
    ]
