# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_auto_20151218_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantbasic',
            name='r_type',
            field=models.CharField(max_length=55),
        ),
    ]
