# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0005_auto_20151125_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beautician',
            name='availability',
            field=models.CharField(blank=True, max_length=2, choices=[(b'A', b'Available'), (b'NA', b'Not Available')]),
        ),
    ]
