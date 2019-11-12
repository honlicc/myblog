#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# date:  2019/11/10 0010
from django.db import models


class BaseModel(models.Model):
    '模型抽象基类'
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')  # 默认未删除

    class Meta:
        '抽象模型类'
        abstract = True
