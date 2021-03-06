# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-11 16:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bus', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bus_trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arriving_time', models.TimeField()),
                ('depature_time', models.TimeField()),
                ('fare', models.DecimalField(decimal_places=2, max_digits=9)),
                ('arriving_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickuparea', to='bus.Stop')),
            ],
        ),
        migrations.RemoveField(
            model_name='bus',
            name='arriving_from',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='arriving_time',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='depature_at',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='depature_time',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='fare',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='id',
        ),
        migrations.AlterField(
            model_name='bus',
            name='bus_number',
            field=models.IntegerField(default=50, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='bus_trip',
            name='bus_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bus.Bus'),
        ),
        migrations.AddField(
            model_name='bus_trip',
            name='depature_at',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='droparea', to='bus.Stop'),
        ),
    ]
