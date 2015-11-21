# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0028_auto_20151121_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='lat',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='lng',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True),
        ),
    ]
