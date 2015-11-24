# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0063_auto_20151124_1749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lead',
            old_name='Services',
            new_name='services',
        ),
        migrations.RemoveField(
            model_name='lead',
            name='action_required',
        ),
        migrations.AddField(
            model_name='order',
            name='source',
            field=models.ForeignKey(blank=True, to='agent.Source', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='supplier',
            field=models.ForeignKey(blank=True, to='agent.Supplier', null=True),
        ),
    ]
