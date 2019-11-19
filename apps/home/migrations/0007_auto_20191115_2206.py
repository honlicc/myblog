# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20191115_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='detail',
            field=models.TextField(verbose_name='详情', blank=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='detail',
            field=models.TextField(verbose_name='详情', blank=True),
        ),
    ]
