# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-06 06:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20171206_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interestarea',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
