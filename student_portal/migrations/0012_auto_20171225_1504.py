# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-25 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_portal', '0011_auto_20171225_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opi_calculated',
            name='opi_value',
            field=models.DecimalField(decimal_places=4, max_digits=20),
        ),
    ]