# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0062_auto_20151124_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.ForeignKey(blank=True, to='agent.City', null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='nearest_station',
            field=models.ForeignKey(blank=True, to='agent.Station', null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.ForeignKey(blank=True, to='agent.State', null=True),
        ),
    ]
