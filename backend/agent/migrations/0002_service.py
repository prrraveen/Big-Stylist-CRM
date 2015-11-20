# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('packages', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('source', models.CharField(max_length=100, blank=True)),
                ('typ', models.CharField(max_length=20, blank=True)),
                ('lp', models.URLField(blank=True)),
            ],
        ),
    ]
