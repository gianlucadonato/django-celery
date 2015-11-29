# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='created_at',
            field=models.DateField(auto_now_add=True),
        ),
    ]
