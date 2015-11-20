# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beautician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('marital_status', models.CharField(max_length=1, choices=[(b'M', b'married'), (b'S', b'Single')])),
                ('family_members', models.CharField(max_length=80, blank=True)),
                ('age', models.IntegerField(null=True, blank=True)),
                ('customer_rating', models.IntegerField(null=True, blank=True)),
                ('bs_rating', models.IntegerField(null=True, blank=True)),
                ('rating_by_service', models.IntegerField(null=True, blank=True)),
                ('phone_number', models.CharField(max_length=11)),
                ('alternate_number', models.CharField(max_length=11, blank=True)),
                ('address', models.CharField(max_length=1000, blank=True)),
                ('locality', models.CharField(max_length=100)),
                ('employment_status', models.CharField(blank=True, max_length=1, choices=[(b'0', b'Employed'), (b'1', b'Unemployed')])),
                ('availability', models.CharField(blank=True, max_length=2, choices=[(b'A', b'Available'), (b'NA', b'Single')])),
                ('Services', models.ManyToManyField(to='agent.Service', null=True, blank=True)),
                ('pincode', models.ForeignKey(related_name='beautician_pincode', blank=True, to='agent.Pincode', null=True)),
                ('serving_in', models.ManyToManyField(related_name='beautician_pincode_server_in', null=True, to='agent.Pincode', blank=True)),
            ],
        ),
    ]
