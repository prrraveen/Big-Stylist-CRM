# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0041_delete_city'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Source',
        ),
        migrations.DeleteModel(
            name='State',
        ),
        migrations.RemoveField(
            model_name='station',
            name='pincode',
        ),
        migrations.DeleteModel(
            name='Supplier',
        ),
        migrations.DeleteModel(
            name='Station',
        ),
    ]
