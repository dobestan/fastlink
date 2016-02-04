# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-04 16:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='이름')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name_plural': '코스',
                'verbose_name': '코스',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hash_id', models.CharField(blank=True, max_length=8, null=True, unique=True)),
                ('url', models.URLField(verbose_name='URL')),
                ('description', models.CharField(max_length=255, verbose_name='설명')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fastlink.Course')),
            ],
            options={
                'verbose_name_plural': '리소스',
                'verbose_name': '리소스',
            },
        ),
    ]