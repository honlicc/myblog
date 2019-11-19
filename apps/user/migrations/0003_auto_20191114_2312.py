# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='desc',
            field=tinymce.models.HTMLField(verbose_name='介绍', blank=True),
        ),
    ]
