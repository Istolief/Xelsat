# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-05 13:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_brand_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='show_in_list',
        ),
    ]
