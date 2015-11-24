# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0036_remove_pincode_localities'),
    ]

    operations = [
        migrations.AddField(
            model_name='pincode',
            name='localities',
            field=models.ManyToManyField(to='agent.Locality', blank=True),
        ),
    ]
