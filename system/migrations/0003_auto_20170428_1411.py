# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-28 14:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20170428_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='add_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='paper',
            name='read_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date read'),
        ),
    ]
