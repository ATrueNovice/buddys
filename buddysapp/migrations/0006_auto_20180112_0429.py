# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-12 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buddysapp', '0005_products_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, upload_to='product_images/'),
        ),
    ]