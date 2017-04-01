# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0012_remove_tollplaza_two_wheeler_toll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tollplaza',
            name='car_jeep_van_toll',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tollplaza',
            name='heavy_vehicle_toll',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tollplaza',
            name='lcv_minibus_toll',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tollplaza',
            name='three_wheeler_toll',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='tollplaza',
            name='toll_latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tollplaza',
            name='toll_longitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='tollplaza',
            name='truck_bus_toll',
            field=models.IntegerField(),
        ),
    ]
