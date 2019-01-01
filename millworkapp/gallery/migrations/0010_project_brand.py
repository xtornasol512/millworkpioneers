# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-28 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_photo_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='brand',
            field=models.CharField(choices=[('MILLWORK', 'Millwork'), ('WOODWORK', 'Woodwork')], default='MILLWORK', help_text='Select the correct!', max_length=100, verbose_name='Company brand'),
        ),
    ]
