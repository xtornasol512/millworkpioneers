# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-02 07:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='email',
            field=models.EmailField(blank=True, max_length=255, verbose_name='Email'),
        ),
    ]
