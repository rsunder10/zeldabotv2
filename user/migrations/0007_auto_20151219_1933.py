# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0020_remove_food_non_veg'),
        ('user', '0006_auto_20151219_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.OneToOneField(to='bot.City', default=1),
            preserve_default=False,
        ),
    ]
