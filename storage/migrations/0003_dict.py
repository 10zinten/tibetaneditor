# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-03 23:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0002_auto_20181228_0225'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=255)),
                ('pos', models.CharField(max_length=255)),
                ('action', models.IntegerField()),
            ],
        ),
    ]