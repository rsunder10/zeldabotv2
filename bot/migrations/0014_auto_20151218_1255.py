# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0013_auto_20151218_1254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantbasic',
            name='area',
            field=models.CharField(max_length=60, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='bookmark',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='checkins',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='city',
            field=models.CharField(max_length=60, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='collections',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='cuisines',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='link',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='r_address',
            field=models.CharField(max_length=300, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='r_name',
            field=models.CharField(max_length=80, blank=True),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='r_type',
            field=models.CharField(max_length=55, blank=True),
        ),
    ]
