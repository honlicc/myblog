# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20191115_2323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='detail',
            field=ckeditor.fields.RichTextField(verbose_name='详情', blank=True),
        ),
        migrations.AlterField(
            model_name='comments',
            name='detail',
            field=ckeditor.fields.RichTextField(verbose_name='详情', blank=True),
        ),
    ]
