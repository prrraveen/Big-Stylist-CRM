# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0011_auto_20151130_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service_type',
            fields=[
                ('name', models.CharField(max_length=30, unique=True, serialize=False, primary_key=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='service',
            name='id',
        ),
        migrations.RemoveField(
            model_name='service',
            name='type',
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=100, unique=True, serialize=False, primary_key=True),
        ),
    ]
