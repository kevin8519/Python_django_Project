# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-19 20:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('gender', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')], default=1, max_length=1)),
                ('address', models.CharField(max_length=200)),
                ('phone', models.IntegerField(max_length=50)),
            ],
        ),
    ]
