# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 07:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docker', '0003_poke_count'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poke',
            old_name='count',
            new_name='counter',
        ),
    ]
