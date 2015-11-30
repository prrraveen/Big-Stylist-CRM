# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0030_remove_package_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='Service',
            field=models.ManyToManyField(to='agent.Service', null=True, blank=True),
        ),
    ]
