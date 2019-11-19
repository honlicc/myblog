# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20191116_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='read',
            field=models.IntegerField(verbose_name='阅读数', default=0),
        ),
    ]
