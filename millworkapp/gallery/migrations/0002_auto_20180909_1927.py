# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-09 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(default='', max_length=255, verbose_name='Photo title')),
                ('description', models.TextField(blank=True, default='', verbose_name='Short description')),
                ('picture', models.ImageField(upload_to='gallery_photos')),
            ],
            options={
                'verbose_name_plural': 'Gallery Page Photos',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', help_text="Prefer use without spaces (Could be with  '_' or '-')", max_length=255, verbose_name='Tag name')),
                ('description', models.CharField(blank=True, default='', max_length=255, verbose_name='Short description')),
            ],
            options={
                'verbose_name_plural': 'Photo Tags',
                'ordering': ['created_at'],
            },
        ),
        migrations.AlterField(
            model_name='review',
            name='place',
            field=models.CharField(blank=True, default='', help_text='Square Image MIN_SIZE=320x320, MAX_SIZE=900x900', max_length=255, verbose_name='Place name'),
        ),
        migrations.AddField(
            model_name='photo',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='photos', to='gallery.Tag'),
        ),
    ]
