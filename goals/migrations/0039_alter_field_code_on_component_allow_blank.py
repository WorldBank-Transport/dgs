# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-11 10:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0038_delete_model_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='component',
            name='code',
            field=models.CharField(blank=True, max_length=10, verbose_name='Component number'),
        ),
    ]
