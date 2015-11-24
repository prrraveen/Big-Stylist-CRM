# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0029_auto_20151121_2054'),
    ]

    operations = [
        migrations.AddField(
            model_name='pincode',
            name='lat',
            field=models.DecimalField(default=1.111, max_digits=10, decimal_places=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pincode',
            name='lng',
            field=models.DecimalField(default=1.11, max_digits=10, decimal_places=6),
            preserve_default=False,
        ),
    ]
