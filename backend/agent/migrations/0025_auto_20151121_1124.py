# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0024_order_allocation_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='allocation_distance',
            field=models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True),
        ),
    ]
