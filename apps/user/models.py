from django.db import models
from db.base_model import BaseModel
from django.contrib.auth.models import AbstractUser
from tinymce.models import HTMLField
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


class UserInfo(BaseModel):
    user = models.ForeignKey('User', verbose_name='所属账户')
    nickname = models.CharField(max_length=50, verbose_name='昵称')
    info = models.CharField(max_length=200, verbose_name='信息')
    face = models.ImageField(upload_to='user', verbose_name='头像')
    job = models.CharField(max_length=20, verbose_name='工作')
    desc = HTMLField(blank=True, verbose_name='介绍')


    class Meta:
        db_table = 'userinfo'
        verbose_name = '个人信息扩展'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname
