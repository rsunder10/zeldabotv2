# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20151219_1934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zelda',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('avatar', models.ImageField(upload_to=user.models.image_upload)),
            ],
        ),
    ]
