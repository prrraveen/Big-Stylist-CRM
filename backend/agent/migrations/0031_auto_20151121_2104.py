# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0030_auto_20151121_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beautician',
            name='pincode',
            field=models.ForeignKey(related_name='beautician_pincode', default=1, to='agent.Pincode'),
            preserve_default=False,
        ),
    ]
