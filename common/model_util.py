# coding=utf-8
'model转化工具类'

from common.exception import ErrorCode

__author__ = 'Jiateng Liang'


def model2dict(obj):
    """
    将model转为dict类型，仅仅适合model!!!
    :param obj:
    :return:
    """
    json_map = {}
    filter = ['query', 'metadata']
    for attr_name in dir(obj):
        value = getattr(obj, attr_name)
        if attr_name not in filter and not attr_name.startswith('__') and not callable(
                value) and not attr_name.startswith('_'):
            if attr_name == 'create_time' or attr_name == 'update_time':
                value = value.strftime('%Y-%m-%d %H:%M:%S')
            json_map[attr_name] = value

    return json_map


def models2dict(obj):
    """
    将model列表转为dict列表
    :param obj:
    :return:
    """
    return [model2dict(o) for o in obj]


def dict2model(obj, dict):
    """
    dict转model
    :param obj: 初始化一个model
    :param dict:
    :return:
    """
    obj.__dict__.update(dict)
    return obj


def json_resp(code=200, msg='success', data=None):
    return {'code': code, 'msg': msg, 'data': data}
