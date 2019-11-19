# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('title', models.CharField(verbose_name='标题', max_length=20)),
                ('image', models.ImageField(verbose_name='图片', upload_to='banner')),
                ('detail', tinymce.models.HTMLField(verbose_name='详情', blank=True)),
                ('status', models.SmallIntegerField(verbose_name='状态', default=1, choices=[(0, '下线'), (1, '上线'), (2, '草稿')])),
                ('user', models.ForeignKey(verbose_name='作者', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '博客',
                'verbose_name_plural': '博客',
                'db_table': 'blog',
            },
        ),
        migrations.CreateModel(
            name='BlogTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('name', models.CharField(verbose_name='名称', max_length=20)),
            ],
            options={
                'verbose_name': '目录列表',
                'verbose_name_plural': '目录列表',
                'db_table': 'bolg_table',
            },
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('name', models.CharField(verbose_name='名称', max_length=20)),
                ('blog', models.ForeignKey(verbose_name='Blog', to='home.Blog')),
                ('table', models.ForeignKey(verbose_name='BlogTable', default='', to='home.BlogTable')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'db_table': 'bolg_tag',
            },
        ),
        migrations.CreateModel(
            name='BlogType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('name', models.CharField(verbose_name='类型名称', max_length=20)),
            ],
            options={
                'verbose_name': 'blog类型',
                'verbose_name_plural': 'blog类型',
                'db_table': 'blog_type',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('detail', tinymce.models.HTMLField(verbose_name='详情', blank=True)),
                ('status', models.SmallIntegerField(verbose_name='状态', default=1, choices=[(0, '删除'), (1, '展示')])),
                ('blog', models.ForeignKey(verbose_name='文章', to='home.Blog')),
                ('user', models.ForeignKey(verbose_name='评论人', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IndexBanner',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('index', models.SmallIntegerField(verbose_name='展示顺序', default=0)),
                ('type', models.ForeignKey(verbose_name='文章', to='home.Blog')),
            ],
            options={
                'verbose_name': '首页轮播图',
                'verbose_name_plural': '首页轮播图',
                'db_table': 'index_banner',
            },
        ),
        migrations.AddField(
            model_name='blogtag',
            name='type',
            field=models.ForeignKey(verbose_name='blog类型', to='home.BlogType'),
        ),
    ]
