# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-07-28 14:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('occupants', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groundtruth',
            name='groundtruthid',
            field=models.AutoField(db_column='GoundTruthId', primary_key=True, serialize=False),
        ),
    ]
