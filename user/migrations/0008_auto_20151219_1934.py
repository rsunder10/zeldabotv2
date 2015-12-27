# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20151219_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='relationship',
        ),
        migrations.AddField(
            model_name='profile',
            name='relationship',
            field=models.OneToOneField(default=1, to='user.Relationship'),
            preserve_default=False,
        ),
    ]
