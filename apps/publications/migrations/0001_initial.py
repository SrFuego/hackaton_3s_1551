# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-06 06:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0003_auto_20171206_0134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('description', models.TextField()),
                ('title', models.CharField(max_length=50, unique=True)),
                ('author', models.ManyToManyField(related_name='publications', to='profiles.Investigator')),
            ],
            options={
                'verbose_name': 'Publicacion',
                'verbose_name_plural': 'Publicaciones',
            },
        ),
        migrations.CreateModel(
            name='PublicationKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de Publicacion',
                'verbose_name_plural': 'Tipos de Publicaciones',
            },
        ),
        migrations.AddField(
            model_name='publication',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publications', to='publications.PublicationKind'),
        ),
    ]