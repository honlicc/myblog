# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20191115_1803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogtype',
            options={'verbose_name': '博客类型', 'verbose_name_plural': '博客类型'},
        ),
        migrations.AddField(
            model_name='blog',
            name='table',
            field=models.ForeignKey(verbose_name='目录', default='', to='home.BlogTable'),
        ),
        migrations.AlterField(
            model_name='blogtag',
            name='type',
            field=models.ForeignKey(verbose_name='博客类型', to='home.BlogType'),
        ),
    ]
