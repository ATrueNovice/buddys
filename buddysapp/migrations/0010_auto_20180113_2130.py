# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-13 21:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buddysapp', '0009_auto_20180113_0549'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
