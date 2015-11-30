# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0028_auto_20151130_1707'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Packages',
            new_name='Package',
        ),
    ]
