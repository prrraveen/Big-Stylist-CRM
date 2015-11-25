# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_squashed_0065_auto_20151124_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='gender',
            field=models.CharField(blank=True, max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')]),
        ),
    ]
