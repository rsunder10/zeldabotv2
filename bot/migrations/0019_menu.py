# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0018_delete_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('food', models.ManyToManyField(to='bot.Food')),
                ('retaurant_basic', models.OneToOneField(to='bot.RestaurantBasic')),
            ],
        ),
    ]
