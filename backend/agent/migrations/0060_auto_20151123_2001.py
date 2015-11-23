# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0059_lead_next_step'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='lead_status',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'Converted'), (2, b'Canceled')]),
        ),
        migrations.AlterField(
            model_name='lead',
            name='next_step',
            field=models.IntegerField(blank=True, null=True, choices=[(1, b'Call back')]),
        ),
    ]
