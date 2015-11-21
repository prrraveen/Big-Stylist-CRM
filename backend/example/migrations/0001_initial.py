# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Markers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=80)),
                ('lat', models.DecimalField(null=True, max_digits=10, decimal_places=6)),
                ('lng', models.DecimalField(null=True, max_digits=10, decimal_places=6)),
            ],
        ),
    ]
