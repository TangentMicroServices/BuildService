# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-22 18:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160522_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metric',
            name='build',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Build'),
        ),
    ]
