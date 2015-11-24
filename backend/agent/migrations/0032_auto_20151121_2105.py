# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0031_auto_20151121_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beautician',
            name='lat',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='beautician',
            name='lng',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True),
        ),
    ]
