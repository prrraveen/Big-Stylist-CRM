# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0064_auto_20151124_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='discount',
            field=models.DecimalField(default=0, null=True, max_digits=7, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='final_price',
            field=models.DecimalField(default=0, null=True, max_digits=7, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='mrp',
            field=models.DecimalField(default=0, null=True, max_digits=7, decimal_places=2, blank=True),
        ),
    ]
