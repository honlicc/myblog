# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20191116_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='详情', default=''),
        ),
        migrations.AlterField(
            model_name='comments',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='详情', default=''),
        ),
    ]
