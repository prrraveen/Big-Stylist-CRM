# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0019_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='beautician',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='services',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
