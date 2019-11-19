# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blog_recommend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='table',
            field=models.ForeignKey(verbose_name='目录', blank=True, null=True, to='home.BlogTable'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='tag',
            field=models.ForeignKey(verbose_name='标签', blank=True, null=True, to='home.BlogTag'),
        ),
    ]
