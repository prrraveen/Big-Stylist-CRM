# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0020_auto_20151120_0839'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2)),
                ('discount', models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2)),
                ('discount_type', models.CharField(max_length=10, blank=True)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Received'), (2, b'Confirmed'), (3, b'Allocated'), (4, b'Cancelled'), (5, b'Rescheduled'), (6, b'Delievered'), (7, b'Feed back and closed'), (8, b'Feedback and closed'), (9, b'Invoice Sent'), (10, b'Money homeward')])),
                ('placedat', models.DateTimeField(null=True, blank=True)),
                ('on', models.DateField(null=True, blank=True)),
                ('at', models.TimeField(null=True, blank=True)),
                ('allocation_status', models.IntegerField(default=1, choices=[(1, b'ToDo'), (2, b'Auto Allocated'), (3, b'Manul Allocated'), (4, b'Accepted'), (5, b'Failed'), (6, b'Cancelled By Beautician')])),
                ('beautician', models.ForeignKey(blank=True, to='agent.Beautician', null=True)),
                ('customer', models.ForeignKey(blank=True, to='agent.Customer', null=True)),
                ('services', models.ManyToManyField(to='agent.Service', null=True, blank=True)),
            ],
        ),
    ]
