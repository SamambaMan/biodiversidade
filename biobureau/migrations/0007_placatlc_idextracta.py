# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-08-26 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biobureau', '0006_auto_20180826_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='placatlc',
            name='idextracta',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
