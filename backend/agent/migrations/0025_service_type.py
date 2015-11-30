# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0024_services_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.ManyToManyField(to='agent.Services_Type', null=True, blank=True),
        ),
    ]
