# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tweet_id', models.BigIntegerField()),
                ('tweet_text', models.TextField()),
                ('tweet_likes', models.IntegerField()),
                ('image_url', models.URLField(max_length=255)),
                ('created_at', models.DateField()),
                ('album', models.ForeignKey(to='albums.Album')),
                ('user', models.ForeignKey(to='users.User')),
            ],
        ),
    ]
