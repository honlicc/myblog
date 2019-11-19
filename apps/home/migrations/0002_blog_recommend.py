# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='recommend',
            field=models.IntegerField(verbose_name='推荐', default=0),
        ),
    ]
