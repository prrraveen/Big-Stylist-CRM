# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0006_remove_beautician_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='beautician',
            name='Services',
            field=models.ManyToManyField(to='agent.Service', null=True, blank=True),
        ),
    ]
