# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produkty', '0003_auto_20161229_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_detail',
            name='memory',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product_detail',
            name='size',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
