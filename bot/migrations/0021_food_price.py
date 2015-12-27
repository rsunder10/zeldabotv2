# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0020_remove_food_non_veg'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='price',
            field=models.IntegerField(default=60),
        ),
    ]
