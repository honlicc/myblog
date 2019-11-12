from django.db import models
from db.base_model import BaseModel
from django.contrib.auth.models import AbstractUser


# Create your models here.
'''
AbstractUser:继承django自带的user类并进行扩展
'''
class User(AbstractUser, BaseModel):
    '''用户模型类'''

    class Meta:
        db_table = 'user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
