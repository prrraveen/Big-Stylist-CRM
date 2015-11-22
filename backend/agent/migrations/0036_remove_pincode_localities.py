# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0035_pincode_localities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pincode',
            name='localities',
        ),
    ]
