# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0022_service_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='service_type',
        ),
    ]
