# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-08 10:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0030_create_model_area_type'),
    ]

    operations = [
        migrations.RemoveField(model_name='area', name='type'),
        migrations.AddField(
            model_name='area',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='areas', to='goals.AreaType', verbose_name='Area type'),
        ),
    ]
