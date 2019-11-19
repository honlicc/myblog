# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20191115_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='detail',
            field=tinymce.models.HTMLField(verbose_name='详情', blank=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(verbose_name='图片', blank=True, upload_to='banner'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='detail',
            field=tinymce.models.HTMLField(verbose_name='详情', blank=True),
        ),
        migrations.AlterField(
            model_name='indexbanner',
            name='image',
            field=models.ImageField(verbose_name='图片', blank=True, upload_to='banner'),
        ),
        migrations.AlterField(
            model_name='indexbanner',
            name='type',
            field=models.ForeignKey(verbose_name='文章', to='home.Blog'),
        ),
    ]
