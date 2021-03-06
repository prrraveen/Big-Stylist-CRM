# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0017_auto_20151120_0836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('gender', models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('contact', models.CharField(max_length=10, blank=True)),
                ('address', models.CharField(max_length=500, blank=True)),
                ('locality', models.ForeignKey(blank=True, to='agent.Locality', null=True)),
                ('pincode', models.ForeignKey(blank=True, to='agent.Pincode', null=True)),
            ],
        ),
    ]
