# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 09:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_meetingroom_office'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='office',
            name='is_available',
        ),
    ]
