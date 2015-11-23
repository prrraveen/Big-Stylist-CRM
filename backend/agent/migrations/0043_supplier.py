# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0042_auto_20151123_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254, serialize=False, primary_key=True)),
                ('contact', models.CharField(max_length=10, blank=True)),
            ],
        ),
    ]
