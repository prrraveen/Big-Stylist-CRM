# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0004_auto_20151125_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='source',
            field=models.ForeignKey(default=1, to='agent.Source'),
            preserve_default=False,
        ),
    ]
