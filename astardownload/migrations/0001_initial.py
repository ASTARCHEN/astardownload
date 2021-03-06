# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-17 05:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='action',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('fileid', models.IntegerField()),
                ('actioncode', models.IntegerField()),
                ('integralschange', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='file',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('filename', models.CharField(max_length=255)),
                ('remotepath', models.CharField(max_length=255)),
                ('tag', models.CharField(max_length=255)),
                ('uploadtime', models.DateTimeField(auto_now_add=True)),
                ('md5', models.CharField(max_length=255)),
                ('abstract', models.CharField(max_length=2048)),
                ('eabstract', models.CharField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('searchstring', models.CharField(max_length=255)),
                ('searchtime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('QQ', models.CharField(max_length=255)),
                ('telephone', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=255)),
                ('realname', models.CharField(max_length=255)),
                ('IDcard', models.CharField(max_length=255)),
                ('registertime', models.DateTimeField(auto_now_add=True)),
                ('integrals', models.IntegerField()),
            ],
        ),
    ]
