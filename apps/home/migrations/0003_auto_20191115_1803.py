# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20191115_1757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogtag',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='blogtag',
            name='table',
        ),
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ForeignKey(verbose_name='标签', default='', to='home.BlogTag'),
        ),
        migrations.AddField(
            model_name='blogtable',
            name='tag',
            field=models.ForeignKey(verbose_name='目录', default='', to='home.BlogTag'),
        ),
    ]
