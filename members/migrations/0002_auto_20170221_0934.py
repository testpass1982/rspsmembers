# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RspsEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(verbose_name='Название события', max_length=100)),
                ('place', models.CharField(verbose_name='Место проведения', max_length=100)),
                ('date', models.DateField(verbose_name='Дата', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'События',
                'verbose_name': 'Событие',
            },
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name_plural': 'Регионы', 'verbose_name': 'Регион'},
        ),
        migrations.AlterModelOptions(
            name='rspsdiv',
            options={'verbose_name_plural': 'Подразделения', 'verbose_name': 'Подразделение'},
        ),
        migrations.AlterModelOptions(
            name='rspsmember',
            options={'verbose_name_plural': 'Члены РСПС', 'verbose_name': 'Член РСПС'},
        ),
        migrations.AlterField(
            model_name='region',
            name='title',
            field=models.CharField(verbose_name='Название', max_length=100),
        ),
        migrations.AlterField(
            model_name='rspsdiv',
            name='region',
            field=models.ForeignKey(verbose_name='Регион', to='members.Region'),
        ),
        migrations.AlterField(
            model_name='rspsmember',
            name='education',
            field=models.CharField(null=True, blank=True, verbose_name='Образование', max_length=200),
        ),
        migrations.AlterField(
            model_name='rspsmember',
            name='first_name',
            field=models.CharField(verbose_name='Имя', max_length=50),
        ),
        migrations.AlterField(
            model_name='rspsmember',
            name='job',
            field=models.CharField(verbose_name='Место работы', max_length=100),
        ),
        migrations.AlterField(
            model_name='rspsmember',
            name='last_name',
            field=models.CharField(verbose_name='Фамилия', max_length=50),
        ),
        migrations.AlterField(
            model_name='rspsmember',
            name='middle_name',
            field=models.CharField(verbose_name='Отчество', max_length=50),
        ),
        migrations.AddField(
            model_name='rspsevents',
            name='rsps_div',
            field=models.ForeignKey(to='members.RspsDiv'),
        ),
    ]
