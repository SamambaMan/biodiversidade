# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-03 02:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listagens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biodiversidade',
            name='obs',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
