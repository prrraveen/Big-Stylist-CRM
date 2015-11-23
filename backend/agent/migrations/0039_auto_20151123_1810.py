# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0038_remove_beautician_serving_in'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Leads',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=20, blank=True)),
                ('last_name', models.CharField(max_length=20, blank=True)),
                ('contact', models.CharField(max_length=10, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('address', models.CharField(max_length=1000, blank=True)),
                ('action_required', models.CharField(max_length=50, blank=True)),
                ('mrp', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
                ('final_price', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
                ('discount', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
                ('discount_type', models.CharField(max_length=10, blank=True)),
                ('lead_status', models.IntegerField(default=1, choices=[(1, b'Received'), (2, b'Confirmed'), (3, b'Allocated'), (4, b'Cancelled'), (5, b'Rescheduled'), (6, b'Delievered'), (7, b'Feed back and closed'), (8, b'Feedback and closed'), (9, b'Invoice Sent'), (10, b'Money homeward')])),
                ('cancellation_reason', models.CharField(max_length=200, blank=True)),
                ('placedat', models.DateTimeField(null=True, blank=True)),
                ('on', models.DateField(null=True, blank=True)),
                ('at', models.TimeField(null=True, blank=True)),
                ('Services', models.ManyToManyField(to='agent.Service', null=True, blank=True)),
                ('assigned_csr', models.ForeignKey(blank=True, to='agent.User', null=True)),
                ('city', models.ForeignKey(blank=True, to='agent.City', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('pincode', models.ForeignKey(to='agent.Pincode')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254, serialize=False, primary_key=True)),
                ('contact', models.CharField(max_length=10, blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, serialize=False, primary_key=True, blank=True),
        ),
        migrations.AddField(
            model_name='leads',
            name='customer',
            field=models.ForeignKey(blank=True, to='agent.Customer', null=True),
        ),
        migrations.AddField(
            model_name='leads',
            name='locality',
            field=models.ForeignKey(blank=True, to='agent.Locality', null=True),
        ),
        migrations.AddField(
            model_name='leads',
            name='nearest_station',
            field=models.ForeignKey(blank=True, to='agent.Station', null=True),
        ),
        migrations.AddField(
            model_name='leads',
            name='pincode',
            field=models.ForeignKey(blank=True, to='agent.Pincode', null=True),
        ),
        migrations.AddField(
            model_name='leads',
            name='source',
            field=models.ForeignKey(blank=True, to='agent.Source', null=True),
        ),
        migrations.AddField(
            model_name='leads',
            name='state',
            field=models.ForeignKey(blank=True, to='agent.State', null=True),
        ),
        migrations.AddField(
            model_name='leads',
            name='supplier',
            field=models.ForeignKey(blank=True, to='agent.Supplier', null=True),
        ),
    ]
