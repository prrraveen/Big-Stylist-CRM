# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0013_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='locality',
            field=models.ForeignKey(blank=True, to='agent.Locality', null=True),
        ),
    ]
