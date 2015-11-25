# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0003_auto_20151125_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(max_length=1000, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='alternate_number',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='contact',
            field=models.CharField(max_length=10, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='emergency_contact',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='emergencyname',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='user',
            name='pincode',
            field=models.ForeignKey(blank=True, to='agent.Pincode', null=True),
        ),
    ]
