# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0014_service_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Service_type',
            new_name='Foo',
        ),
        migrations.AddField(
            model_name='service',
            name='type',
            field=models.ManyToManyField(to='agent.Foo', null=True, blank=True),
        ),
    ]
