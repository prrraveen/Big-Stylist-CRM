# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0016_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='locality',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
