# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0054_lead'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='last_name',
        ),
        migrations.AddField(
            model_name='lead',
            name='name',
            field=models.CharField(max_length=50, blank=True),
        ),
    ]
