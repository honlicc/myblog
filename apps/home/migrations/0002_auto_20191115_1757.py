# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
        migrations.AlterModelTable(
            name='comments',
            table='Comments',
        ),
    ]
