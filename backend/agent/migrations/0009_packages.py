# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0008_auto_20151130_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=50)),
                ('weekday', models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2)),
                ('weekend', models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2)),
                ('Service', models.ManyToManyField(to='agent.Service', null=True, blank=True)),
            ],
        ),
    ]
