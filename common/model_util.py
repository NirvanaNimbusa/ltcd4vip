# coding=utf-8
'model转化工具类'
from common.exception import ErrorCode

__author__ = 'Jiateng Liang'


def model2dict(obj):
    """
    将model转为dict类型
    :param obj:
    :return:
    """
    json_map = {}
    filter = ['query', 'metadata']
    for attr_name in dir(obj):
        value = getattr(obj, attr_name)
        if attr_name not in filter and not attr_name.startswith('__') and not callable(
                value) and not attr_name.startswith('_'):
            json_map[attr_name] = value

    return json_map


def dict2model(obj, dict):
    """
    dict转model
    :param obj: 初始化一个model
    :param dict:
    :return:
    """
    obj.__dict__.update(dict)
    return obj


def json_resp(obj):
    data = model2dict(obj)
    return {'code': ErrorCode.SUCCESS, 'msg': 'success', 'data': data}
