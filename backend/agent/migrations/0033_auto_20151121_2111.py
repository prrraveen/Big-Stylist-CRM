# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0032_auto_20151121_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pincode',
            name='localities',
            field=models.ManyToManyField(to='agent.Locality', null=True, blank=True),
        ),
    ]
