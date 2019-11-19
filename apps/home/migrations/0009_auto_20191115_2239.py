# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20191115_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='detail',
            field=models.TextField(verbose_name='详情', blank=True),
        ),
    ]
