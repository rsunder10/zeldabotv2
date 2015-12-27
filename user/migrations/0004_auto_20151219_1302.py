# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_profile_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='realtionship',
            new_name='relationship',
        ),
    ]
