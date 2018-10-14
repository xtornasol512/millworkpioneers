# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-14 01:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0008_auto_20181014_0016'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='service',
            field=models.ForeignKey(blank=True, help_text='Select one Service', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='photos', to='gallery.Service'),
        ),
    ]
