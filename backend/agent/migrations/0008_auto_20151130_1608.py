# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0007_remove_service_packages'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(0)),
        ),
        migrations.AddField(
            model_name='service',
            name='gender',
            field=models.CharField(blank=True, max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'U', b'Unisex')]),
        ),
    ]
