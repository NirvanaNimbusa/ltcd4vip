#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'comment'
import os

from flask import make_response, redirect, request

__author__ = 'Jiateng Liang'
from bootstrap_init import app


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    file_path = os.getcwd() + request.path

    if os.path.isdir(file_path):
        if not file_path.endswith('/'):
            # 对于没有以'/'进行结尾的情况，进行重定向，从而文件路径可以正确获取
            return redirect(request.url + '/')
        file_path = file_path + 'index.html'

    if not os.path.isfile(file_path):
        return u'该文件或者目录不存在'

    with open(file_path, 'rb') as f:
        body = f.read()

    response = make_response(body)
    if file_path.endswith('.css'):
        response.headers.set('Content-Type', 'text/css')
    elif file_path.endswith('.js'):
        response.headers.set('Content-Type', 'application/javascript')
    return response
