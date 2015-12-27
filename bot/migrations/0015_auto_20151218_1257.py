# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0014_auto_20151218_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantbasic',
            name='bookmark',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='checkins',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='r_name',
            field=models.CharField(max_length=80),
        ),
    ]
