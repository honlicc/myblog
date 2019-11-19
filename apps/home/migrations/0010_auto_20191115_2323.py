# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20191115_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='detail',
            field=tinymce.models.HTMLField(verbose_name='详情', blank=True),
        ),
    ]
