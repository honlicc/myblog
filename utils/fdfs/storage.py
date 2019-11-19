#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# date:  2019/9/14 0014
from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client
from django.conf import settings


class FDSStorage(Storage):

    def __init__(self, client_conf=None, base_url=None):
        if client_conf is None:
            client_conf = settings.FDFS_CLIENT_CONF
        if base_url is None:
            base_url = settings.FDFS_URL

        self.client_conf = client_conf
        self.base_url = base_url

    def _open(self, name, mode='rb'):
        pass

    def _save(self, name, content):
        client = Fdfs_client(self.client_conf)

        res = client.upload_by_buffer(content.read())

        # {
        #     'Group name': group_name,
        #     'Remote file_id': remote_file_id,
        #     'Status': 'Upload successed.',
        #     'Local file name': '',
        #     'Uploaded size': upload_size,
        #     'Storage IP': storage_ip
        # } if success else None

        if res.get('Status') != 'Upload successed.':
            # 上传失败
            raise Exception('上传文件到fasr dfs失败')

        filename = res.get('Remote file_id')

        return filename

    def exists(self, name):
        return False

    def url(self, name):
        return self.base_url + name
