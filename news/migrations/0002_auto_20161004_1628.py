# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-04 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.FileField(default='None', upload_to=''),
        ),
        migrations.AddField(
            model_name='post',
            name='lead',
            field=models.CharField(default='', max_length=200),
        ),
    ]
