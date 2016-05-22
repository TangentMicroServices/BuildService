# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-22 08:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BooleanMetric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200)),
                ('value', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('build_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('default', None), ('percent', 'percent')], default=None, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Repo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Smell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_name', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('remediation', models.IntegerField()),
                ('description', models.CharField(max_length=200)),
                ('issue_type', models.CharField(max_length=200)),
                ('engine', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SmellCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('smell', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.Smell')),
            ],
        ),
        migrations.AddField(
            model_name='metric',
            name='build',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.Repo'),
        ),
        migrations.AddField(
            model_name='build',
            name='repo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.Repo'),
        ),
        migrations.AddField(
            model_name='booleanmetric',
            name='build',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ui.Repo'),
        ),
    ]
