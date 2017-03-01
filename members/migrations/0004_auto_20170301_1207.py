# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_auto_20170222_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='rspsdiv',
            name='created_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='has_division',
            field=models.BooleanField(verbose_name='Есть подразделение'),
        ),
        migrations.AlterField(
            model_name='rspsdiv',
            name='telephone',
            field=models.CharField(max_length=50, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='rspsdiv',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]
