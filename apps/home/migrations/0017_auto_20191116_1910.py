# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20191116_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(verbose_name='图片', blank=True, null=True, upload_to='banner'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='table',
            field=models.ForeignKey(verbose_name='目录', blank=True, null=True, to='home.BlogTable'),
        ),
    ]
