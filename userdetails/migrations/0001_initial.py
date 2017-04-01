# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 06:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RfidCar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfid_no', models.CharField(max_length=20, unique=True)),
                ('number_plate', models.CharField(default=b'', max_length=10, unique=True)),
                ('car_name', models.CharField(max_length=20)),
                ('car_type', models.CharField(max_length=20)),
                ('chassis_no', models.CharField(max_length=20)),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('expiry_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TollPlaza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toll_name', models.CharField(default=b'', max_length=100)),
                ('toll_latitude', models.CharField(max_length=10)),
                ('toll_longitude', models.CharField(max_length=10)),
                ('two_wheeler_toll', models.IntegerField()),
                ('three_wheeler_toll', models.IntegerField()),
                ('car_jeep_van_toll', models.IntegerField()),
                ('lcv_minibus_toll', models.IntegerField()),
                ('truck_bus_toll', models.IntegerField()),
                ('heavy_vehicle_toll', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_no', models.CharField(max_length=20)),
                ('transaction_date_time', models.DateTimeField(blank=True, null=True)),
                ('amount_paid', models.IntegerField(default=0)),
                ('payment_status', models.BooleanField(default=False)),
                ('rfid_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdetails.RfidCar')),
                ('toll', models.ForeignKey(default=b'', on_delete=django.db.models.deletion.CASCADE, to='userdetails.TollPlaza')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserRfid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfid_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userdetails.RfidCar')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
