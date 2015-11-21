# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0026_auto_20151121_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='pincode',
            field=models.ForeignKey(to='agent.Pincode', null=True),
        ),
    ]
