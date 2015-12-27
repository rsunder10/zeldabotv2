# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0004_restaurantbasics'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RestaurantBasics',
            new_name='RestaurantBasic',
        ),
    ]
