# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0017_auto_20151130_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='type',
        ),
    ]
