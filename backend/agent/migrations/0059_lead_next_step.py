# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0058_auto_20151123_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='next_step',
            field=models.IntegerField(default=1, blank=True, choices=[(1, b'Call back')]),
        ),
    ]
