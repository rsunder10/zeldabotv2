# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20151219_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='active',
        ),
    ]
