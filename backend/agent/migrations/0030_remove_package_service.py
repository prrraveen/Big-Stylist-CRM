# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0029_auto_20151130_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='Service',
        ),
    ]
