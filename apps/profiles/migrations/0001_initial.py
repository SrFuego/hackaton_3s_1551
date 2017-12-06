# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-06 04:27
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InterestArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Area de Interes',
                'verbose_name_plural': 'Areas de Interes',
            },
        ),
        migrations.CreateModel(
            name='Investigator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('graduated', models.BooleanField(default=False)),
                ('orcid_code', models.CharField(blank=True, max_length=16)),
                ('role', models.CharField(choices=[('undergraduate', 'Pregrado'), ('bachelor', 'Bachiller'), ('professor', 'Docente'), ('postgraduate', 'Postgrado')], max_length=15)),
                ('unmsm_code', models.CharField(max_length=8, unique=True)),
                ('interest_areas', models.ManyToManyField(blank=True, to='profiles.InterestArea')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Investigador',
                'verbose_name_plural': 'Investigadores',
            },
        ),
    ]
