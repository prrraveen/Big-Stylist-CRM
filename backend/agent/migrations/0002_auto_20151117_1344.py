# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='at',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='beautician',
            field=models.ForeignKey(blank=True, to='agent.Beautician', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='on',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='placedat',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
