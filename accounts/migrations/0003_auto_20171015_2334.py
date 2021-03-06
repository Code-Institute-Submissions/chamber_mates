# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 22:34
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20171013_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326),
        ),
        migrations.AlterField(
            model_name='profile',
            name='max_distance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Distance'),
        ),
    ]
