# coding=utf-8
'日志，全局统一用logger'

from logging.handlers import TimedRotatingFileHandler

__author__ = 'Jiateng Liang'
from bootstrap import app

import logging

logger = logging.getLogger(app.config['LOG_NAME'])

fh = TimedRotatingFileHandler(filename=app.config['LOG_PATH'], when="D", interval=1)

if app.config['LOG_LEVEL'] == 'DEBUG':
    logger.setLevel(logging.DEBUG)
    fh.setLevel(logging.DEBUG)
elif app.config['LOG_LEVEL'] == 'INFO':
    logger.setLevel(logging.INFO)
    fh.setLevel(logging.INFO)
elif app.config['LOG_LEVEL'] == 'WARN':
    logger.setLevel(logging.WARN)
    fh.setLevel(logging.WARN)
elif app.config['LOG_LEVEL'] == 'ERROR':
    logger.setLevel(logging.ERROR)
    fh.setLevel(logging.ERROR)

formatter = logging.Formatter(app.config['LOG_FORMAT'], app.config['LOG_DATE_FORMAT'])

fh.setFormatter(formatter)
logger.addHandler(fh)

if app.config['LOG_CONSOLE']:
    console = logging.StreamHandler()
    console.setLevel(app.config['LOG_LEVEL'])
    console.setFormatter(formatter)
    logger.addHandler(console)
