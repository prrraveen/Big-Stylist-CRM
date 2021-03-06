# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0027_auto_20151130_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='beautician',
            name='Services',
            field=models.ManyToManyField(to='agent.Service', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='services',
            field=models.ManyToManyField(to='agent.Service', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='services',
            field=models.ManyToManyField(to='agent.Service', null=True, blank=True),
        ),
    ]
