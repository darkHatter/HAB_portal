# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-31 06:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student_portal', '0013_auto_20171225_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messfeedback',
            name='username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]