#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# date:  2019/11/11 0011
from celery import Celery
from blog import settings
from django.core.mail import send_mail


import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
django.setup()


app = Celery('celery_tasks.tasks', broker='redis://192.168.83.128:6379/8')

#celery + redis 异步发送邮件
@app.task
def send_register_active_email(to_email, username, token):
    '''发送激活邮件'''
    # 发送邮件

    subject = 'Hello'  # 邮件标题
    message = ''
    send_name = settings.EMAIL_FROM  # 发件人
    receiver = [to_email]  # 收件人，元祖或列表
    html_message = '<h1>%s:欢迎来到宏利的博客</h1><br/>请点击以下链接完成账号激活<br/><a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>' % (
        username, token, token)

    send_mail(subject=subject, message=message, from_email=send_name, recipient_list=receiver,
              html_message=html_message)