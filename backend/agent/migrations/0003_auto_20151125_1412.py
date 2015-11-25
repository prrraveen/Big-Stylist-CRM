# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0002_auto_20151125_0846'),
    ]

    operations = [
        migrations.AddField(
            model_name='beautician',
            name='employee_id',
            field=models.CharField(max_length=30, blank=True),
        ),
        migrations.AddField(
            model_name='beautician',
            name='station',
            field=models.ForeignKey(blank=True, to='agent.Station', null=True),
        ),
        migrations.AddField(
            model_name='beautician',
            name='type',
            field=models.CharField(blank=True, max_length=2, choices=[(b'1', b'Free Agent'), (b'2', b'Minimum Guarantee')]),
        ),
    ]
