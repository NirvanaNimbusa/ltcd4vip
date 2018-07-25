# coding=utf-8
'自定义异常'
import functools
import traceback
from datetime import datetime
from common.log import logger
from bootstrap_init import db

__author__ = 'Jiateng Liang'


class ErrorCode(object):
    FAIL = -1
    INTERNAL_ERROR = 5
    SUCCESS = 1
    NOT_FOUND = 4
    PARAM_ERROR = 3


class ServiceException(Exception):
    def __init__(self, error_code, msg='', detail=''):
        Exception.__init__(self, msg)
        self.error_code = error_code
        self.time = str(datetime.now())
        self.msg = msg
        self.detail = detail

    def get_log_msg(self):
        return '时间：' + self.time + '；错误码：' + str(self.error_code) + '；错误信息：' + self.msg + '；详情：' + self.detail


# 异常捕捉器
def api(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        try:
            return func(*args, **kw)
        except Exception as e:
            if isinstance(e, ServiceException):
                if e.error_code < 5:
                    logger.warn(e.get_log_msg())
                else:
                    logger.fatal(e.get_log_msg())
            else:
                exstr = traceback.format_exc()
                logger.fatal(str(e) + '\n详情：' + exstr)
            db.session.rollback()
        finally:
            db.session.close()

    return wrapper
