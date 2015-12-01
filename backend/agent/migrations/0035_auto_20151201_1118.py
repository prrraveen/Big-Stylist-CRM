# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0034_auto_20151130_1811'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='beautician',
            name='unavailable_on',
            field=models.ManyToManyField(to='agent.Days', null=True, blank=True),
        ),
    ]
