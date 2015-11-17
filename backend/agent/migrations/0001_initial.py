# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
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
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, blank=True)),
                ('gender', models.CharField(default=b'M', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('contact', models.CharField(max_length=10, blank=True)),
                ('address', models.CharField(max_length=500, blank=True)),
                ('locality', models.CharField(max_length=100, blank=True)),
                ('pincode', models.CharField(max_length=10, blank=True)),
                ('nearest_station', models.CharField(max_length=10, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2)),
                ('discount', models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2)),
                ('discount_type', models.CharField(max_length=10, blank=True)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Received'), (2, b'Confirmed'), (3, b'Allocated'), (4, b'Cancelled'), (5, b'Rescheduled'), (6, b'Delievered'), (7, b'Feedback and closed'), (8, b'Feedback and closed'), (9, b'Invoice Sent'), (10, b'Money homeward')])),
                ('customer', models.ForeignKey(blank=True, to='agent.Customer', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('services', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('source', models.CharField(max_length=100, blank=True)),
                ('typ', models.CharField(max_length=20, blank=True)),
                ('lp', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=80)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='services',
            field=models.ManyToManyField(to='agent.Service', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='beautician',
            name='services',
            field=models.ManyToManyField(to='agent.Service'),
        ),
    ]
