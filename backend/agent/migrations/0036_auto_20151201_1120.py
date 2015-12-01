# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0035_auto_20151201_1118'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Days',
            new_name='Day',
        ),
    ]
