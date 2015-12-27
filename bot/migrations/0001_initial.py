# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RestaurantBasics',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('r_name', models.CharField(default='', max_length=80)),
                ('area', models.CharField(default='', max_length=60)),
                ('bookmark', models.IntegerField(default=0)),
                ('checkins', models.IntegerField(default=0)),
                ('city', models.CharField(max_length=60)),
                ('collections', models.CharField(max_length=100)),
                ('cuisines', models.CharField(max_length=100)),
                ('r_address', models.CharField(max_length=300)),
                ('link', models.URLField()),
                ('photos', models.IntegerField(default=0)),
                ('r_id', models.IntegerField(default=0)),
                ('r_latitude', models.DecimalField(max_digits=10, decimal_places=5, default=0)),
                ('r_longitude', models.DecimalField(max_digits=10, decimal_places=5, default=0)),
                ('rating', models.IntegerField(default=0)),
                ('rating_votes', models.IntegerField(default=0)),
                ('reviews', models.IntegerField(default=0)),
                ('r_type', models.CharField(max_length=50)),
            ],
        ),
    ]
