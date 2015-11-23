# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0055_auto_20151123_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='requirment',
            field=models.CharField(max_length=300, blank=True),
        ),
    ]
