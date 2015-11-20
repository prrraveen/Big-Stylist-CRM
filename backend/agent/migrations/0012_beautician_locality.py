# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0011_remove_beautician_locality'),
    ]

    operations = [
        migrations.AddField(
            model_name='beautician',
            name='locality',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
