# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20170221_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='rspsevents',
            name='body',
            field=models.TextField(default='Описание события', verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='rspsevents',
            name='rsps_div',
            field=models.ForeignKey(verbose_name='Подразделение', to='members.RspsDiv'),
        ),
        migrations.AlterField(
            model_name='rspsmember',
            name='is_a_leader',
            field=models.BooleanField(verbose_name='Руководитель'),
        ),
        migrations.AlterField(
            model_name='rspsmember',
            name='rsps_div',
            field=models.ForeignKey(verbose_name='Подразделение', to='members.RspsDiv'),
        ),
    ]
