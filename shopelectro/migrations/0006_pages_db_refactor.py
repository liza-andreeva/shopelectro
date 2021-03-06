# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-11 11:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopelectro', '0005_remove_null_True_from_text_fields'),
        ('pages', '0005_db_refactor')
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='category',
            name='page',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shopelectro_category', to='pages.Page'),
        ),
        migrations.AlterField(
            model_name='product',
            name='page',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shopelectro_product', to='pages.Page'),
        ),
        migrations.RemoveField(
            model_name='category',
            name='position',
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='product',
            name='in_stock',
            field=models.BooleanField(db_index=True, default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='is_popular',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.CreateModel(
            name='CategoryPage',
            fields=[
            ],
            options={
                'abstract': False,
                'proxy': True,
            },
            bases=('pages.modelpage',),
        ),
        migrations.CreateModel(
            name='ProductPage',
            fields=[
            ],
            options={
                'abstract': False,
                'proxy': True,
            },
            bases=('pages.modelpage',),
        ),
        migrations.AlterField(
            model_name='property',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
