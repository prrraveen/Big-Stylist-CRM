# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0025_service_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='type',
        ),
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.ForeignKey(blank=True, to='agent.Services_Type', null=True),
        ),
    ]
