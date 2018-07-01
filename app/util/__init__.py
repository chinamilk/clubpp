# -*-coding:utf-8-*-
"""常用的功能方法

"""
import json
import uuid
from datetime import datetime, date
from json import JSONEncoder

from app.api import BaseDto


class ComplexEncoder(JSONEncoder):
    """针对复杂类的转JSON方式进行扩展, 如果特定类型没有进行覆盖，请在default方法中自行拓展.

    """
    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        elif isinstance(o, set):
            return json.dumps(list(o))
        elif isinstance(o, BaseDto):
            return o.__dict__
        else:
            return JSONEncoder.default(self, o)


def obj2json(obj) -> str:
    """根据实例属性，将python对象转化为json字符串。

    :param obj: 要被转化的对象
    :return: json字符串
    """

    return json.dumps(obj, cls=ComplexEncoder, ensure_ascii=False)


def map_path_to_url(filepath: str) -> str:
    """map the filepath of the file(image...) to the http url.

    :param filepath: the absolute logical path of the file (the path field of <user> table and <club> table)
    :return: the http url
    """
    pass


def generate_uuid():
    """Generate a unique id for record.

    :return: uuid value
    """
    return uuid.uuid4().hex
