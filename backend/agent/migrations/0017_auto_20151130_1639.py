# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0016_auto_20151130_1638'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service_Type',
            new_name='Services_Type',
        ),
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.ManyToManyField(to='agent.Services_Type', null=True, blank=True),
        ),
    ]
