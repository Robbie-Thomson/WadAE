# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-03 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATGApp', '0004_auto_20190301_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stadium',
            name='postcode',
            field=models.CharField(max_length=20),
        ),
    ]
