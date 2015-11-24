# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0040_auto_20151123_1814'),
    ]

    operations = [
        migrations.DeleteModel(
            name='City',
        ),
    ]
