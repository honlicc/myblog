# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20191116_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='table',
            field=models.ForeignKey(verbose_name='目录', blank=True, to='home.BlogTable'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='tag',
            field=models.ForeignKey(verbose_name='标签', to='home.BlogTag'),
        ),
        migrations.AlterField(
            model_name='blogtable',
            name='tag',
            field=models.ForeignKey(verbose_name='目录', to='home.BlogTag'),
        ),
    ]
