# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20170715_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/home/static/img/cogorange.png', upload_to=''),
        ),
    ]