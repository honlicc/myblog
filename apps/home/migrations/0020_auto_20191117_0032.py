# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_blogtag_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='user',
            field=models.ForeignKey(verbose_name='作者', to='user.UserInfo'),
        ),
    ]
