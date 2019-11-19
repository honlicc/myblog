# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20191115_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexbanner',
            name='image',
            field=models.ImageField(verbose_name='图片', default='', upload_to='banner'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(verbose_name='图片', blank=True, default='', upload_to='banner'),
        ),
        migrations.AlterField(
            model_name='indexbanner',
            name='type',
            field=models.ForeignKey(verbose_name='文章', to='home.BlogType'),
        ),
    ]
