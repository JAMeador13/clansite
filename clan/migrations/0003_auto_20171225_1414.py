# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-25 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clan', '0002_participant_displayname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='character',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ParticipationInstances', to='clan.Character'),
        ),
    ]