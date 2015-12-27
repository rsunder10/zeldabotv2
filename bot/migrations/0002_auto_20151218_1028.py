# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantbasics',
            name='area',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='restaurantbasics',
            name='photos',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='restaurantbasics',
            name='r_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='restaurantbasics',
            name='r_latitude',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='restaurantbasics',
            name='r_longitude',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='restaurantbasics',
            name='r_name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='restaurantbasics',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='restaurantbasics',
            name='rating_votes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='restaurantbasics',
            name='reviews',
            field=models.IntegerField(),
        ),
    ]
