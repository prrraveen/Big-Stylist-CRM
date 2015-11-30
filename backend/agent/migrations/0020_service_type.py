# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0019_delete_services_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
