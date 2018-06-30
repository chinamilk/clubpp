# -*-coding:utf-8-*-
"""常用的功能方法

"""
import json


def obj2json(obj) -> str:
    """根据实例属性，将python对象转化为json字符串。

    :param obj: 要被转化的对象
    :return: json字符串
    """

    return json.dumps(obj, default=lambda instance: instance.__dict__, ensure_ascii=False)


def map_path_to_url(filepath: str) -> str:
    """map the filepath of the file(image...) to the http url.

    :param filepath: the absolute logical path of the file (the path field of <user> table and <club> table)
    :return: the http url
    """
    pass
