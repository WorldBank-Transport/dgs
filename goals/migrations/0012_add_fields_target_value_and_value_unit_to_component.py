# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0011_add_stats_available_default_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='progress',
            name='value_unit',
        ),
        migrations.AddField(
            model_name='component',
            name='target_value',
            field=models.FloatField(blank=True, null=True, verbose_name='Target value'),
        ),
        migrations.AddField(
            model_name='component',
            name='value_unit',
            field=models.CharField(blank=True, max_length=50, verbose_name='Value unit'),
        ),
    ]