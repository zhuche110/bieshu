# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-16 09:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20170416_0849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Potho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='\u56fe\u7247\u8bf4\u660e', max_length=100, verbose_name='\u6807\u9898')),
                ('order', models.CharField(max_length=10, verbose_name='\u6392\u5e8f\u6807\u5fd7')),
                ('if_cover', models.CharField(choices=[('1', '\u662f'), ('0', '\u5426')], default='0', max_length=10, verbose_name='\u662f\u5426\u8bbe\u7f6e\u4e3a\u5c01\u9762\u56fe\u7247')),
                ('images', models.ImageField(upload_to='static/photos')),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.House')),
            ],
        ),
    ]
