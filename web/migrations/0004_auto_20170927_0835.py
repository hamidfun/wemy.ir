# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-09-27 08:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20170927_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='posts/%Y/%m/%d', verbose_name='main image'),
        ),
    ]
