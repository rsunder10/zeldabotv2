# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0007_auto_20151218_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantbasic',
            name='cost',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
