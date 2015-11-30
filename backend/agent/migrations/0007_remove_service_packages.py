# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0006_auto_20151126_1252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='packages',
        ),
    ]
