# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-01 17:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_homelogoheader'),
    ]

    operations = [
        migrations.AddField(
            model_name='homelogoheader',
            name='site_url',
            field=models.URLField(blank=True, default='#', verbose_name='Site url'),
        ),
    ]