# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-29 08:34
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0006_paper_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name=''),
        ),
    ]
