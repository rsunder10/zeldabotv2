# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0005_auto_20151218_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantbasic',
            name='bookmark',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='checkins',
            field=models.IntegerField(),
        ),
    ]
