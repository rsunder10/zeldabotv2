# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0009_auto_20151218_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantbasic',
            name='cost',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='photos',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='r_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='reviews',
            field=models.IntegerField(blank=True),
        ),
    ]
