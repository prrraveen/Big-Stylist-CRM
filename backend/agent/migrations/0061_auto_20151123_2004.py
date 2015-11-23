# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0060_auto_20151123_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='lead_status',
            field=models.IntegerField(default=1, choices=[(1, b'No lead status yet'), (2, b'Converted'), (3, b'Canceled')]),
        ),
        migrations.AlterField(
            model_name='lead',
            name='next_step',
            field=models.IntegerField(default=1, choices=[(1, b'No next step yet'), (2, b'Call back')]),
        ),
    ]
