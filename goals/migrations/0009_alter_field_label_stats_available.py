# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0008_alter_slug_add_blank_true'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='stats_available',
            field=models.CharField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No'), ('PARTIALLY', 'Partially'), ('UNKNOWN', 'Unknown')], max_length=50, verbose_name='Statistics availble'),
        ),
    ]