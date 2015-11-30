# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0023_delete_service_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services_Type',
            fields=[
                ('name', models.CharField(max_length=30, serialize=False, primary_key=True)),
            ],
        ),
    ]
