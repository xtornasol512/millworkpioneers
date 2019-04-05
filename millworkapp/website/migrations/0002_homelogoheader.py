# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-24 21:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeLogoHeader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='', max_length=255, verbose_name='Photo title')),
                ('description', models.TextField(default='', help_text='This help on SEO, use a brief description of logo', verbose_name='Short description')),
                ('picture', models.ImageField(help_text='Must have to be edited before, 900x506 pixeles! For better quality', upload_to='home_photos_header')),
                ('is_display_on_website', models.BooleanField(default=True, help_text='Select "Yes" to display on site', verbose_name='Will display on site?')),
                ('page', models.ForeignKey(blank=True, help_text='Select Home Page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='page_header_photos', to='website.HomePage')),
            ],
            options={
                'verbose_name_plural': 'Home Website Header Logos',
                'ordering': ['-created_at'],
            },
        ),
    ]
