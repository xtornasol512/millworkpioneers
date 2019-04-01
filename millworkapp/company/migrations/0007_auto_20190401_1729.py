# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-01 17:29
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_company_gmaps'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='bid_due',
            field=models.DateField(default=datetime.datetime.today, verbose_name='Bid due date'),
        ),
    ]
