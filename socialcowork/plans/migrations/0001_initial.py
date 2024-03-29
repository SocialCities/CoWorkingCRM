# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 10:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0003_remove_office_is_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
                ('meeting_room_hours', models.IntegerField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('days_per_month', models.IntegerField(blank=True, null=True)),
                ('type_of_plan', models.CharField(choices=[('HD', 'Hot Desk'), ('FD', 'Fix Desk'), ('PO', 'Private Office')], max_length=3)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locations.Location')),
                ('office', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.Office')),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Plans',
            },
        ),
    ]
