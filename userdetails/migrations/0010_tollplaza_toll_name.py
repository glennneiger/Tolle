# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0009_remove_tollplaza_toll_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tollplaza',
            name='toll_name',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
