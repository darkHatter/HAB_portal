# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-23 21:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FinalPreference',
            fields=[
                ('hostelName', models.CharField(choices=[('Barak', 'Barak'), ('Bramhaputra', 'Bramhaputra'), ('Dhansiri', 'Dhansiri'), ('Dibang', 'Dibang'), ('Dihing', 'Dihing'), ('Kameng', 'Kameng'), ('Kapili', 'Kapili'), ('Lohit', 'Lohit'), ('Manas', 'Manas'), ('Siang', 'Siang'), ('Subansiri', 'Subansiri'), ('Umiam', 'Umiam'), ('NA', 'NA')], max_length=255)),
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('final_hostel', models.CharField(choices=[('Barak', 'Barak'), ('Bramhaputra', 'Bramhaputra'), ('Dhansiri', 'Dhansiri'), ('Dibang', 'Dibang'), ('Dihing', 'Dihing'), ('Kameng', 'Kameng'), ('Kapili', 'Kapili'), ('Lohit', 'Lohit'), ('Manas', 'Manas'), ('Siang', 'Siang'), ('Subansiri', 'Subansiri'), ('Umiam', 'Umiam'), ('NA', 'NA')], max_length=255)),
            ],
            options={
                'verbose_name': 'FinalPreference',
                'verbose_name_plural': 'FinalPreference',
            },
        ),
        migrations.CreateModel(
            name='MessFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostelName', models.CharField(choices=[('Barak', 'Barak'), ('Bramhaputra', 'Bramhaputra'), ('Dhansiri', 'Dhansiri'), ('Dibang', 'Dibang'), ('Dihing', 'Dihing'), ('Kameng', 'Kameng'), ('Kapili', 'Kapili'), ('Lohit', 'Lohit'), ('Manas', 'Manas'), ('Siang', 'Siang'), ('Subansiri', 'Subansiri'), ('Umiam', 'Umiam'), ('NA', 'NA')], max_length=255)),
                ('cleanliness', models.IntegerField(choices=[(0, 'Very Poor'), (1, 'Poor'), (2, 'Average'), (3, 'Neutral'), (4, 'Good'), (5, 'Very Good')], null=True)),
                ('qual_b', models.IntegerField(choices=[(0, 'Very Poor'), (1, 'Poor'), (2, 'Average'), (3, 'Neutral'), (4, 'Good'), (5, 'Very Good')], null=True)),
                ('qual_l', models.IntegerField(choices=[(0, 'Very Poor'), (1, 'Poor'), (2, 'Average'), (3, 'Neutral'), (4, 'Good'), (5, 'Very Good')], null=True)),
                ('qual_d', models.IntegerField(choices=[(0, 'Very Poor'), (1, 'Poor'), (2, 'Average'), (3, 'Neutral'), (4, 'Good'), (5, 'Very Good')], null=True)),
                ('catering', models.IntegerField(choices=[(0, 'Very Poor'), (1, 'Poor'), (2, 'Average'), (3, 'Neutral'), (4, 'Good'), (5, 'Very Good')], null=True)),
                ('filled', models.BooleanField(default=False)),
                ('month', models.IntegerField(default=12)),
                ('year', models.IntegerField(default=2017)),
                ('comment', models.TextField()),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('username', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'MessFeedback',
                'verbose_name_plural': 'MessFeedback',
            },
        ),
        migrations.CreateModel(
            name='Opi_calculated',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostelName', models.CharField(choices=[('Barak', 'Barak'), ('Bramhaputra', 'Bramhaputra'), ('Dhansiri', 'Dhansiri'), ('Dibang', 'Dibang'), ('Dihing', 'Dihing'), ('Kameng', 'Kameng'), ('Kapili', 'Kapili'), ('Lohit', 'Lohit'), ('Manas', 'Manas'), ('Siang', 'Siang'), ('Subansiri', 'Subansiri'), ('Umiam', 'Umiam'), ('NA', 'NA')], max_length=255)),
                ('opi_value', models.DecimalField(decimal_places=2, max_digits=20)),
                ('numberOfSubscriptions', models.IntegerField()),
                ('month', models.IntegerField(default=12)),
                ('year', models.IntegerField(default=2017)),
                ('cleanliness_av', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('breakfast_quality_av', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('lunch_quality_av', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('dinner_quality_av', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('catering_av', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('raw_materials_quality', models.IntegerField(choices=[(0, 'Very Poor'), (1, 'Poor'), (2, 'Average'), (3, 'Neutral'), (4, 'Good'), (5, 'Very Good')], null=True)),
            ],
            options={
                'verbose_name': 'Opi_calculated',
                'verbose_name_plural': 'Opi_calculated',
            },
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('hostelName', models.CharField(choices=[('Barak', 'Barak'), ('Bramhaputra', 'Bramhaputra'), ('Dhansiri', 'Dhansiri'), ('Dibang', 'Dibang'), ('Dihing', 'Dihing'), ('Kameng', 'Kameng'), ('Kapili', 'Kapili'), ('Lohit', 'Lohit'), ('Manas', 'Manas'), ('Siang', 'Siang'), ('Subansiri', 'Subansiri'), ('Umiam', 'Umiam'), ('NA', 'NA')], max_length=255)),
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('month', models.IntegerField(default=2)),
                ('year', models.IntegerField(default=2018)),
                ('h1', models.CharField(choices=[('Barak', 'Barak'), ('Bramhaputra', 'Bramhaputra'), ('Dhansiri', 'Dhansiri'), ('Dibang', 'Dibang'), ('Dihing', 'Dihing'), ('Kameng', 'Kameng'), ('Kapili', 'Kapili'), ('Lohit', 'Lohit'), ('Manas', 'Manas'), ('Siang', 'Siang'), ('Subansiri', 'Subansiri'), ('Umiam', 'Umiam'), ('NA', 'NA')], max_length=255)),
                ('h2', models.CharField(choices=[('Barak', 'Barak'), ('Bramhaputra', 'Bramhaputra'), ('Dhansiri', 'Dhansiri'), ('Dibang', 'Dibang'), ('Dihing', 'Dihing'), ('Kameng', 'Kameng'), ('Kapili', 'Kapili'), ('Lohit', 'Lohit'), ('Manas', 'Manas'), ('Siang', 'Siang'), ('Subansiri', 'Subansiri'), ('Umiam', 'Umiam'), ('NA', 'NA')], max_length=255)),
                ('h3', models.CharField(choices=[('Barak', 'Barak'), ('Bramhaputra', 'Bramhaputra'), ('Dhansiri', 'Dhansiri'), ('Dibang', 'Dibang'), ('Dihing', 'Dihing'), ('Kameng', 'Kameng'), ('Kapili', 'Kapili'), ('Lohit', 'Lohit'), ('Manas', 'Manas'), ('Siang', 'Siang'), ('Subansiri', 'Subansiri'), ('Umiam', 'Umiam'), ('NA', 'NA')], max_length=255)),
            ],
            options={
                'verbose_name': 'Preferences',
                'verbose_name_plural': 'Preferences',
            },
        ),
        migrations.AlterUniqueTogether(
            name='preference',
            unique_together=set([('username', 'month', 'year')]),
        ),
        migrations.AlterUniqueTogether(
            name='opi_calculated',
            unique_together=set([('hostelName', 'month', 'year')]),
        ),
        migrations.AlterUniqueTogether(
            name='finalpreference',
            unique_together=set([('username', 'month', 'year')]),
        ),
        migrations.AlterUniqueTogether(
            name='messfeedback',
            unique_together=set([('username', 'month', 'year')]),
        ),
    ]
