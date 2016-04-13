# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20160413_1042'),
    ]

    operations = [
        migrations.CreateModel(
            name='Create_opportunity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(default=0, upload_to='static/image', verbose_name='My Photo', blank=True)),
                ('title', models.CharField(max_length=140)),
                ('location', models.CharField(max_length=140)),
                ('description', models.TextField(null=True)),
                ('skills_needed', models.CharField(max_length=140, blank=True)),
                ('hours_required', models.CharField(max_length=140, blank=True)),
                ('days', models.CharField(max_length=140, blank=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
