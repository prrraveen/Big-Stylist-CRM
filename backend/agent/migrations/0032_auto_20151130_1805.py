# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0031_package_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
