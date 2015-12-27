# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0002_auto_20151218_1028'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RestaurantBasics',
        ),
    ]
