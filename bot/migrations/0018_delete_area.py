# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_profile_area'),
        ('bot', '0017_area_city_food_type'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Area',
        ),
    ]
