# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('nickname', models.CharField(verbose_name='昵称', max_length=50)),
                ('info', models.CharField(verbose_name='信息', max_length=200)),
                ('face', models.ImageField(verbose_name='头像', upload_to='user')),
                ('job', models.CharField(verbose_name='工作', max_length=20)),
                ('desc', models.CharField(verbose_name='介绍', max_length=200)),
                ('user', models.ForeignKey(verbose_name='所属账户', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '个人信息扩展',
                'verbose_name_plural': '个人信息扩展',
                'db_table': 'userinfo',
            },
        ),
    ]
