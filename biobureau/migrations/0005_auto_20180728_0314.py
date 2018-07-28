# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-07-28 03:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biobureau', '0004_auto_20180728_0305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partedeplanta',
            name='cheiro',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='partedeplanta',
            name='cor',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='partedeplanta',
            name='notas',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='partedeplanta',
            name='peso',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
