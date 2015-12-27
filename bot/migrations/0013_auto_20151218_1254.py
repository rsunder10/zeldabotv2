# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0012_auto_20151218_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantbasic',
            name='r_latitude',
            field=models.DecimalField(blank=True, max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='r_longitude',
            field=models.DecimalField(blank=True, max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='rating',
            field=models.DecimalField(blank=True, max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='rating_votes',
            field=models.DecimalField(blank=True, max_digits=10, decimal_places=5),
        ),
    ]
