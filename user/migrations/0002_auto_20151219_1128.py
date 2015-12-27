# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0017_area_city_food_type'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('status', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='area',
            field=models.ManyToManyField(to='bot.Area'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.ManyToManyField(to='bot.City'),
        ),
        migrations.AddField(
            model_name='profile',
            name='fav_food',
            field=models.ManyToManyField(to='bot.Food'),
        ),
        migrations.AddField(
            model_name='profile',
            name='preferrs',
            field=models.ManyToManyField(to='bot.Type'),
        ),
        migrations.AddField(
            model_name='profile',
            name='realtionship',
            field=models.ManyToManyField(to='user.Relationship'),
        ),
    ]
