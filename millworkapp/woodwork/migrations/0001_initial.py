# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-28 04:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WoodworkPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='website_header')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(blank=True, default='Wodwork Page', max_length=255, verbose_name='Page title')),
            ],
            options={
                'verbose_name_plural': 'Woodwork Page',
                'ordering': ['-created_at'],
            },
        ),
    ]
