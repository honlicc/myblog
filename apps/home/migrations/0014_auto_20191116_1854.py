# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20191116_1830'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='blogtable',
            table='blog_table',
        ),
        migrations.AlterModelTable(
            name='blogtag',
            table='blog_tag',
        ),
    ]
