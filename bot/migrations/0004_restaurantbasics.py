# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_delete_restaurantbasics'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantBasics',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('r_name', models.CharField(max_length=80)),
                ('area', models.CharField(max_length=60)),
                ('bookmark', models.IntegerField(default=0)),
                ('checkins', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=60)),
                ('collections', models.CharField(max_length=100)),
                ('cuisines', models.CharField(max_length=100)),
                ('r_address', models.CharField(max_length=300)),
                ('link', models.URLField()),
                ('photos', models.IntegerField()),
                ('r_id', models.IntegerField()),
                ('r_latitude', models.DecimalField(max_digits=10, decimal_places=5)),
                ('r_longitude', models.DecimalField(max_digits=10, decimal_places=5)),
                ('rating', models.IntegerField()),
                ('rating_votes', models.IntegerField()),
                ('reviews', models.IntegerField()),
                ('r_type', models.CharField(max_length=50)),
            ],
        ),
    ]
