# -*-coding:utf-8-*-
"""处理API请求的类都写在这个包里，按资源对API进行分类，写在不同的文件中，之后在main.py中注册为URL请求映射。建议API的
    响应json设计为字典或者对象，字段设计为键或者属性，使用相关JSON包导出为json字符串，避免使用字符串拼接。

"""


class BaseDto:
    """对于需要使用obj2json方法转JSON的dto类， 都必须继承本类

    """
    pass
