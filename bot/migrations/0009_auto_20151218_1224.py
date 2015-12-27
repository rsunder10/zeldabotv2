# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0008_restaurantbasic_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantbasic',
            name='rating',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
        migrations.AlterField(
            model_name='restaurantbasic',
            name='rating_votes',
            field=models.DecimalField(max_digits=10, decimal_places=5),
        ),
    ]
