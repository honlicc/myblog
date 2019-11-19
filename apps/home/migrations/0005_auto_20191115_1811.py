# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20191115_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='table',
            field=models.ForeignKey(verbose_name='目录', blank=True, default='', to='home.BlogTable'),
        ),
    ]
