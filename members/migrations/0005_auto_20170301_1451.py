# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_auto_20170301_1207'),
    ]

    operations = [
        migrations.AddField(
            model_name='rspsmember',
            name='created_date',
            field=models.DateField(verbose_name='Дата принятия', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='rspsdiv',
            name='created_date',
            field=models.DateTimeField(verbose_name='Дата создания', null=True, blank=True),
        ),
    ]
