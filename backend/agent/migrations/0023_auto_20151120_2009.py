# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0022_auto_20151120_1940'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='lat',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=6),
        ),
        migrations.AddField(
            model_name='customer',
            name='lng',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=6),
        ),
    ]
