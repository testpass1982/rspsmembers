# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('has_division', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='RspsDiv',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('telephone', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('region', models.ForeignKey(to='members.Region')),
            ],
        ),
        migrations.CreateModel(
            name='RspsMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=100)),
                ('is_a_leader', models.BooleanField()),
                ('education', models.CharField(max_length=200)),
                ('rsps_div', models.ForeignKey(to='members.RspsDiv')),
            ],
        ),
    ]
