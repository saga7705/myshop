# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20161221_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, upload_to='product'),
        ),
    ]
