# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0025_auto_20151121_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='skiped_beautician',
            field=models.ManyToManyField(related_name='skiped_beautician', null=True, to='agent.Beautician', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='beautician',
            field=models.ForeignKey(related_name='allocated', blank=True, to='agent.Beautician', null=True),
        ),
    ]
