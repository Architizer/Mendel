# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-13 18:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mendel', '0001_squashed_0004_auto_20160510_1825'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Content',
            new_name='Context',
        ),
    ]
