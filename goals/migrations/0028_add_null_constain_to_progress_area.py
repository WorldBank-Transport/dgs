# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 09:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def add_default_area(apps, schema_editor):
    """Use a dummy area for progress with no areas
    """
    Area = apps.get_model('goals', 'Area')
    Progress = apps.get_model('goals', 'Progress')
    prgs = Progress.objects.filter(area=None)
    if len(prgs):
        area = Area.objects.first()
        for progress in prgs:
            progress.area = area
            progress.save()


def dummy(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('goals', '0027_modify_translated_fields'),
    ]

    operations = [
        migrations.RunPython(add_default_area, reverse_code=dummy),
        migrations.AlterField(
            model_name='progress',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='progress', to='goals.Area', verbose_name='Area'),
        ),
    ]
