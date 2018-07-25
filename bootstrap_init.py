# coding=utf-8
'初始化应用，防止循环引用'
__author__ = 'Jiateng Liang'
from flask import Flask, Blueprint
from config.config import *
from flask_sqlalchemy import SQLAlchemy
import sys

app = Flask(__name__)

# 配置文件 环境设置
if len(sys.argv) <= 1 or sys.argv[1] == 'dev':
    app.config.from_object(Config)
elif sys.argv[1] == 'test':
    app.config.from_object(TestConfig)
elif sys.argv[1] == 'prod':
    app.config.from_pyfile(ProdConfig)

# 数据库初始化
db = SQLAlchemy(app)


