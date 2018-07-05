# -*-coding:utf-8-*-
"""常用的功能方法

"""
import json
import uuid
import jwt
from datetime import datetime, date
from json import JSONEncoder
from app import WWW_ROOT, BASIC_URL, DATE_PATTERN, DATETIME_PATTERN, SECRET_KEY
from app.api import BaseDto
from flask import make_response, request
from app.dao import user_dao


class ComplexEncoder(JSONEncoder):
    """针对复杂类的转JSON方式进行扩展, 如果特定类型没有进行覆盖，请在default方法中自行拓展.

    """

    def default(self, o):
        if isinstance(o, datetime):
            return o.strftime(DATETIME_PATTERN)
        elif isinstance(o, date):
            return o.strftime(DATE_PATTERN)
        elif isinstance(o, set):
            return json.dumps(list(o))
        elif isinstance(o, BaseDto):
            return o.__dict__
        else:
            return JSONEncoder.default(self, o)


def obj2json(obj) -> dict:
    """根据实例属性，将python对象转化为json字典。

    :param obj: 要被转化的对象
    :return: json 字典
    """

    return json.loads(json.dumps(obj, cls=ComplexEncoder, ensure_ascii=False))


def map_path_to_url(filepath: str) -> str:
    """map the filepath of the file(image...) to the http url.

    :param filepath: the absolute logical path of the file (the path field of <user> table and <club> table)
    :return: the http url
    """
    relative_path = filepath.replace(WWW_ROOT, "")
    return BASIC_URL + relative_path


def generate_uuid():
    """Generate a unique id for record.

    :return: uuid value
    """
    return uuid.uuid4().hex


def login_required(func):
    """
    verify jwt
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        token = request.headers.get('x-auth-token')
        try:
            jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            make_response("token timeout!!", 401)
            return
        except jwt.InvalidTokenError:
            make_response("invalid token!!", 400)
            return
        except Exception:
            make_response("unknown exception!!", 400)
            return
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    def wrapper(*args, **kwargs):
        request_data_dict = eval(str(request.data, encoding="utf8").replace('\n', '').replace('\t', ''))
        username = request_data_dict['username']
        is_admin = user_dao.get_is_admin_by_username(username)
        if is_admin:
            return func(*args, **kwargs)
        make_response('需要管理员权限！', 403)

    return wrapper


def str2date(date_str: str):
    """Convert string to date.

    :param date_str: date string
    :return:
    """
    return datetime.strptime(date_str, DATE_PATTERN).date()


def add_attribute(obj: object, name: str, value, default_value=None) -> object:
    """Add the attribute to the obj if the value is not equal to default_value given.

    :param obj: the object
    :param name: the name of the field
    :param value: the value of the field
    :param default_value: the default value
    :return: the obj
    """
    if value != default_value:
        obj.__setattr__(name, value)
    return obj
