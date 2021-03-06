# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-05 09:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_href',
            field=models.URLField(blank=True, null=True, verbose_name='Link Εικόνας Mymoda.gr'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Αρχική Τιμή'),
        ),
        migrations.AlterField(
            model_name='product',
            name='price_discount',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=6, verbose_name='Τιμή Έκπτωσης'),
        ),
        migrations.AlterField(
            model_name='product',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='Περιγραφή'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Τίτλος'),
        ),
    ]
