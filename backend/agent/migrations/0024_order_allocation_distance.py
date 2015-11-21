# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0023_auto_20151120_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='allocation_distance',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2),
        ),
    ]
