# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-01 09:04
from __future__ import unicode_literals

from django.db import migrations, models
import homepage.models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20171025_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='about_description',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_keywords',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='about_title',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='background_image',
            field=models.ImageField(blank=True, help_text='1400px*800px', null=True, upload_to=homepage.models.upload_background_banner, validators=[homepage.models.validate_size]),
        ),
        migrations.AddField(
            model_name='homepage',
            name='blog_description',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='blog_keywords',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='blog_title',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='store_description',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='store_keywords',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='store_title',
            field=models.CharField(blank=True, max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name='circleimages',
            name='image',
            field=models.ImageField(help_text='370px*370px', upload_to=homepage.models.upload_location, validators=[homepage.models.validate_size_normal]),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='circle_image',
            field=models.ImageField(blank=True, help_text='1920px * 794px', null=True, upload_to=homepage.models.upload_location, validators=[homepage.models.validate_size_normal]),
        ),
        migrations.AlterField(
            model_name='mainbanner',
            name='image',
            field=models.ImageField(upload_to=homepage.models.upload_location, validators=[homepage.models.validate_size_normal], verbose_name='Είκονα'),
        ),
    ]