# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0015_auto_20151130_1637'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Foo',
            new_name='Service_Type',
        ),
        migrations.RemoveField(
            model_name='service',
            name='type',
        ),
    ]
