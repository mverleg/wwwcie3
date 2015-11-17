# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
                ('topic', models.CharField(max_length=20)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
=======
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now=True)),
                ('text', models.TextField()),
>>>>>>> origin/master
            ],
        ),
        migrations.CreateModel(
            name='ChatTopic',
            fields=[
<<<<<<< HEAD
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=20)),
            ],
        ),
=======
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.SlugField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='topic',
            field=models.ForeignKey(to='chatz.ChatTopic'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
>>>>>>> origin/master
    ]
