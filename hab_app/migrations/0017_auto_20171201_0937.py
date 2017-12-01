# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-01 09:37
from __future__ import unicode_literals

from django.db import migrations, models
import hab_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('hab_app', '0016_auto_20171111_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupantdetails',
            name='idPhoto',
            field=models.ImageField(blank=True, upload_to='id_pics', validators=[hab_app.models.OccupantDetails.validate_image]),
        ),
        migrations.AlterField(
            model_name='occupantdetails',
            name='photo',
            field=models.ImageField(blank=True, upload_to='profile_pics', validators=[hab_app.models.OccupantDetails.validate_image]),
        ),
    ]