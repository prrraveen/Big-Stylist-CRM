# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0009_packages'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='typ',
            new_name='type',
        ),
    ]
