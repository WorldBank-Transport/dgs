# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-23 18:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0048_add_translation_fields_to_theme_sector_and_sectortype_models'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicator',
            name='sector',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='indicators', to='goals.Sector', verbose_name='Sector'),
        ),
    ]
