# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2018-12-05 22:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0006_auto_20181205_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='enemy',
        ),
    ]