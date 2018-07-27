# coding=utf-8
'配置文件，无需重复配置，不存在的配置默认配置会覆盖'
__author__ = 'Jiateng Liang'


class Config(object):
    """
    默认配置
    """
    AUTHOR = 'Jiateng Liang'
    # 应用配置
    HTTP_HEAD = 'http://'
    HTTP_HOST = '127.0.0.1'
    HTTP_PORT = 5000
    SECRET_KEY = 'ltcd4vip-dev'
    WTF_CSRF_ENABLED = False
    # 数据库配置
    DB_USERNAME = 'root'
    DB_PASSWORD = '123456'
    DB_HOST = '127.0.0.1'
    DB_NAME = 'blog'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://' + DB_USERNAME + ':' + DB_PASSWORD + '@' + DB_HOST + '/' + DB_NAME + '?charset=utf8'
    ENABLE_SQL_LOG = True

    # 日志配置
    LOG_NAME = 'ltcd4vip'
    LOG_CONSOLE = True  # 是否打印到控制台
    LOG_LEVEL = 'DEBUG'  # DEBUG INFO WARN ERROR
    LOG_PATH = '/Users/liangjiateng/Desktop/log.log'
    LOG_FORMAT = '%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s'
    LOG_DATE_FORMAT = "%a %d %b %Y %H:%M:%S"

    # 分页设置
    PAGE_SMALL = 10
    PAGE_MEDIUM = 25
    PAGE_LARGE = 50

    # LeetCode账号集群
    LEETCODE_ACCOUNTS = ['luxuan.wang@nyu.edu', '525=xuan']


class TestConfig(Config):
    """
    测试环境配置
    """
    # 应用配置
    HTTP_HOST = '0.0.0.0'
    HTTP_PORT = 12580
    SECRET_KEY = 'ltcd4vip-test'

    # 日志配置
    LOG_CONSOLE = False
    LOG_PATH = '../log/ltcd4vip/log.log'

    # 数据库
    # DB_USERNAME = 'liangjiateng_blog_prod'
    # DB_PASSWORD = '71E36E4C76607A954FEC1DC390EDAE57'


class ProdConfig(Config):
    """
    生产环境配置
    """
    # 应用配置
    HTTP_HOST = 'www.liangjiateng.cn'
    HTTP_PORT = 12306
    SECRET_KEY = 'ltcd4vip-prod'
