# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0021_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='beautician',
            name='lat',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=6),
        ),
        migrations.AddField(
            model_name='beautician',
            name='lng',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=6),
        ),
    ]
