# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-07 06:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sensorvalues', '0005_sensorvalues_ult_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='sensorvalues',
            name='water_value',
            field=models.CharField(default=100, max_length=250),
            preserve_default=False,
        ),
    ]