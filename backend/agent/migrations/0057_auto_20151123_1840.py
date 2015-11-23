# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0056_lead_requirment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='lead_status',
            field=models.IntegerField(default=1, choices=[(1, b'Converted'), (2, b'Canceled')]),
        ),
    ]
