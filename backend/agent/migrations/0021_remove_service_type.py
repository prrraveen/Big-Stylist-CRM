# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0020_service_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='type',
        ),
    ]
