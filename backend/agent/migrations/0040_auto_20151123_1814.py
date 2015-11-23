# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0039_auto_20151123_1810'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leads',
            name='Services',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='assigned_csr',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='city',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='nearest_station',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='pincode',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='source',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='state',
        ),
        migrations.RemoveField(
            model_name='leads',
            name='supplier',
        ),
        migrations.DeleteModel(
            name='Leads',
        ),
    ]
