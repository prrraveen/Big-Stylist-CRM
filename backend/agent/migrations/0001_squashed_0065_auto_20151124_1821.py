# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [(b'agent', '0001_initial'), (b'agent', '0002_service'), (b'agent', '0003_beautician'), (b'agent', '0004_auto_20151120_0721'), (b'agent', '0005_beautician_pincode'), (b'agent', '0006_remove_beautician_services'), (b'agent', '0007_beautician_services'), (b'agent', '0008_beautician_serving_in'), (b'agent', '0009_remove_beautician_locality'), (b'agent', '0010_beautician_locality'), (b'agent', '0011_remove_beautician_locality'), (b'agent', '0012_beautician_locality'), (b'agent', '0013_customer'), (b'agent', '0014_customer_locality'), (b'agent', '0015_auto_20151120_0833'), (b'agent', '0016_customer'), (b'agent', '0017_auto_20151120_0836'), (b'agent', '0018_customer'), (b'agent', '0019_order'), (b'agent', '0020_auto_20151120_0839'), (b'agent', '0021_order'), (b'agent', '0022_auto_20151120_1940'), (b'agent', '0023_auto_20151120_2009'), (b'agent', '0024_order_allocation_distance'), (b'agent', '0025_auto_20151121_1124'), (b'agent', '0026_auto_20151121_1620'), (b'agent', '0027_auto_20151121_2046'), (b'agent', '0028_auto_20151121_2052'), (b'agent', '0029_auto_20151121_2054'), (b'agent', '0030_auto_20151121_2100'), (b'agent', '0031_auto_20151121_2104'), (b'agent', '0032_auto_20151121_2105'), (b'agent', '0033_auto_20151121_2111'), (b'agent', '0034_remove_pincode_localities'), (b'agent', '0035_pincode_localities'), (b'agent', '0036_remove_pincode_localities'), (b'agent', '0037_pincode_localities'), (b'agent', '0038_remove_beautician_serving_in'), (b'agent', '0039_auto_20151123_1810'), (b'agent', '0040_auto_20151123_1814'), (b'agent', '0041_delete_city'), (b'agent', '0042_auto_20151123_1814'), (b'agent', '0043_supplier'), (b'agent', '0044_source'), (b'agent', '0045_station'), (b'agent', '0046_state'), (b'agent', '0047_city'), (b'agent', '0048_leads'), (b'agent', '0049_auto_20151123_1818'), (b'agent', '0050_customer_email'), (b'agent', '0051_auto_20151123_1829'), (b'agent', '0052_auto_20151123_1830'), (b'agent', '0053_auto_20151123_1833'), (b'agent', '0054_lead'), (b'agent', '0055_auto_20151123_1837'), (b'agent', '0056_lead_requirment'), (b'agent', '0057_auto_20151123_1840'), (b'agent', '0058_auto_20151123_1841'), (b'agent', '0059_lead_next_step'), (b'agent', '0060_auto_20151123_2001'), (b'agent', '0061_auto_20151123_2004'), (b'agent', '0062_auto_20151124_1652'), (b'agent', '0063_auto_20151124_1749'), (b'agent', '0064_auto_20151124_1749'), (b'agent', '0065_auto_20151124_1821')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Locality',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Pincode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pincode', models.CharField(max_length=6)),
                ('localities', models.ManyToManyField(to=b'agent.Locality')),
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
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('packages', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('source', models.CharField(max_length=100, blank=True)),
                ('typ', models.CharField(max_length=20, blank=True)),
                ('lp', models.URLField(blank=True)),
            ],
        ),
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
                ('employment_status', models.CharField(blank=True, max_length=1, choices=[(b'0', b'Employed'), (b'1', b'Unemployed')])),
                ('availability', models.CharField(blank=True, max_length=2, choices=[(b'A', b'Available'), (b'NA', b'Single')])),
                ('pincode', models.ForeignKey(related_name='beautician_pincode', blank=True, to='agent.Pincode', null=True)),
                ('Services', models.ManyToManyField(to=b'agent.Service', null=True, blank=True)),
                ('serving_in', models.ManyToManyField(related_name='beautician_pincode_server_in', null=True, to=b'agent.Pincode', blank=True)),
                ('locality', models.CharField(max_length=100, blank=True)),
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
                ('locality', models.ForeignKey(blank=True, to='agent.Locality', null=True)),
                ('pincode', models.ForeignKey(blank=True, to='agent.Pincode', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amount', models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2)),
                ('discount', models.DecimalField(default=0, null=True, max_digits=10, decimal_places=2)),
                ('discount_type', models.CharField(max_length=10, blank=True)),
                ('status', models.IntegerField(default=1, choices=[(1, b'Received'), (2, b'Confirmed'), (3, b'Allocated'), (4, b'Cancelled'), (5, b'Rescheduled'), (6, b'Delievered'), (7, b'Feed back and closed'), (8, b'Feedback and closed'), (9, b'Invoice Sent'), (10, b'Money homeward')])),
                ('placedat', models.DateTimeField(null=True, blank=True)),
                ('on', models.DateField(null=True, blank=True)),
                ('at', models.TimeField(null=True, blank=True)),
                ('allocation_status', models.IntegerField(default=1, choices=[(1, b'ToDo'), (2, b'Auto Allocated'), (3, b'Manul Allocated'), (4, b'Accepted'), (5, b'Failed'), (6, b'Cancelled By Beautician')])),
                ('beautician', models.ForeignKey(blank=True, to='agent.Beautician', null=True)),
                ('customer', models.ForeignKey(blank=True, to='agent.Customer', null=True)),
                ('services', models.ManyToManyField(to=b'agent.Service', null=True, blank=True)),
                ('allocation_distance', models.DecimalField(null=True, max_digits=5, decimal_places=2, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='beautician',
            name='lat',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True),
        ),
        migrations.AddField(
            model_name='beautician',
            name='lng',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='lat',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='lng',
            field=models.DecimalField(null=True, max_digits=10, decimal_places=6, blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='skiped_beautician',
            field=models.ManyToManyField(related_name='skiped_beautician', null=True, to=b'agent.Beautician', blank=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='beautician',
            field=models.ForeignKey(related_name='allocated', blank=True, to='agent.Beautician', null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='pincode',
            field=models.ForeignKey(to='agent.Pincode', null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='pincode',
            field=models.ForeignKey(default=1, to='agent.Pincode'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pincode',
            name='lat',
            field=models.DecimalField(default=1.111, max_digits=10, decimal_places=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pincode',
            name='lng',
            field=models.DecimalField(default=1.11, max_digits=10, decimal_places=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beautician',
            name='pincode',
            field=models.ForeignKey(related_name='beautician_pincode', default=1, to='agent.Pincode'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='pincode',
            name='localities',
        ),
        migrations.AddField(
            model_name='pincode',
            name='localities',
            field=models.ManyToManyField(to=b'agent.Locality', blank=True),
        ),
        migrations.RemoveField(
            model_name='beautician',
            name='serving_in',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='id',
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254, serialize=False, primary_key=True)),
                ('contact', models.CharField(max_length=10, blank=True)),
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
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('pincode', models.ForeignKey(to='agent.Pincode')),
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
            name='City',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact', models.CharField(max_length=10, blank=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('gender', models.CharField(max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('address', models.CharField(max_length=1000, blank=True)),
                ('mrp', models.DecimalField(default=0, null=True, max_digits=7, decimal_places=2, blank=True)),
                ('final_price', models.DecimalField(default=0, null=True, max_digits=7, decimal_places=2, blank=True)),
                ('discount', models.DecimalField(default=0, null=True, max_digits=7, decimal_places=2, blank=True)),
                ('discount_type', models.CharField(max_length=10, blank=True)),
                ('lead_status', models.IntegerField(default=1, choices=[(1, b'No lead status yet'), (2, b'Converted'), (3, b'Canceled')])),
                ('cancellation_reason', models.CharField(max_length=200, blank=True)),
                ('placedat', models.DateTimeField(null=True, blank=True)),
                ('on', models.DateField(null=True, blank=True)),
                ('at', models.TimeField(null=True, blank=True)),
                ('services', models.ManyToManyField(to=b'agent.Service', null=True, blank=True)),
                ('assigned_csr', models.ForeignKey(blank=True, to='agent.User', null=True)),
                ('city', models.ForeignKey(blank=True, to='agent.City', null=True)),
                ('customer', models.ForeignKey(blank=True, to='agent.Customer', null=True)),
                ('locality', models.ForeignKey(blank=True, to='agent.Locality', null=True)),
                ('nearest_station', models.ForeignKey(blank=True, to='agent.Station', null=True)),
                ('pincode', models.ForeignKey(blank=True, to='agent.Pincode', null=True)),
                ('source', models.ForeignKey(blank=True, to='agent.Source', null=True)),
                ('state', models.ForeignKey(blank=True, to='agent.State', null=True)),
                ('supplier', models.ForeignKey(blank=True, to='agent.Supplier', null=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('requirment', models.CharField(max_length=300, blank=True)),
                ('next_step', models.IntegerField(default=1, choices=[(1, b'No next step yet'), (2, b'Call back')])),
            ],
        ),
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
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.ForeignKey(blank=True, to='agent.City', null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='nearest_station',
            field=models.ForeignKey(blank=True, to='agent.Station', null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.ForeignKey(blank=True, to='agent.State', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='source',
            field=models.ForeignKey(blank=True, to='agent.Source', null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='supplier',
            field=models.ForeignKey(blank=True, to='agent.Supplier', null=True),
        ),
    ]
