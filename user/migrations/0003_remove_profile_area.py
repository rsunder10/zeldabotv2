# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20151219_1128'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='area',
        ),
    ]
