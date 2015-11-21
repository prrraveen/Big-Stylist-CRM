# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0027_auto_20151121_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pincode',
            field=models.ForeignKey(default=1, to='agent.Pincode'),
            preserve_default=False,
        ),
    ]
