# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_blog_read'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogtag',
            name='image',
            field=models.ImageField(verbose_name='图片', blank=True, upload_to='tag'),
        ),
    ]
