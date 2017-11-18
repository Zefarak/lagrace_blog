# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-25 07:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('keywords', models.CharField(blank=True, max_length=150, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=150, null=True)),
                ('context', tinymce.models.HTMLField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_edited', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('alt', models.CharField(blank=True, max_length=150, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_edited', models.DateTimeField(auto_now=True)),
                ('post_related', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Brands')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='')),
                ('keywords', models.CharField(blank=True, max_length=150, null=True)),
                ('meta_description', models.CharField(blank=True, max_length=150, null=True)),
                ('context', tinymce.models.HTMLField(blank=True, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('date_edited', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AddField(
            model_name='brands',
            name='post_related',
            field=models.ManyToManyField(to='blog.Post'),
        ),
    ]