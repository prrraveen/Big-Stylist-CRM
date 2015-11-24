# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0061_auto_20151123_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='beautician_feedback',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='bs_commission',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='client_feedback',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='collected',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='how_was_client',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='how_was_service',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='net_from_supplier_to_bs',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='notes',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='quality_of_Service',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='rate_supplier',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='remarks',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='supplier_commission',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='supplier_feedback',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='supplier_remark',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='was_supplier_on_time',
            field=models.CharField(max_length=20, blank=True),
        ),
    ]
