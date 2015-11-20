# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0004_auto_20151120_0721'),
    ]

    operations = [
        migrations.AddField(
            model_name='beautician',
            name='pincode',
            field=models.ForeignKey(related_name='beautician_pincode', blank=True, to='agent.Pincode', null=True),
        ),
    ]
