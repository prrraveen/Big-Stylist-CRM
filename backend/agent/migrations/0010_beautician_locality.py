# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0009_remove_beautician_locality'),
    ]

    operations = [
        migrations.AddField(
            model_name='beautician',
            name='locality',
            field=models.ForeignKey(blank=True, to='agent.Locality', null=True),
        ),
    ]
