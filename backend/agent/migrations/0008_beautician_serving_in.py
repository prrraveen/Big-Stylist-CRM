# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0007_beautician_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='beautician',
            name='serving_in',
            field=models.ManyToManyField(related_name='beautician_pincode_server_in', null=True, to='agent.Pincode', blank=True),
        ),
    ]
