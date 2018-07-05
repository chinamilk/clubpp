# -*-coding:utf-8-*-
"""处理API请求的类都写在这个包里，按资源对API进行分类，写在不同的文件中，之后在main.py中注册为URL请求映射。建议API的
    响应json设计为字典或者对象，字段设计为键或者属性，使用相关JSON包导出为json字符串，避免使用字符串拼接。

"""


class BaseDto:
    """对于需要使用obj2json方法转JSON的dto类， 都必须继承本类

    """
    pass


class ClubDto(BaseDto):
    """club接口数据传输对象.
       对应的json数据格式为:
       {
          "club_id": "uuid",
          "club_name": "xxx club",
          "created_date": "2000-01-03",
          "member_number": 123,
          "club_bio": "这是一个社团。",
          "tags": "a,b,c",
          "addresses": "addr1,addr2,addr3",
          "master_id": "uuid",
          "images": [
            {
              "url": "url1",
              "club_id": "uuid",
              "image_id": "uuin"
            },
            {
              "url": "url2",
              "club_id": "uuid",
              "image_id": "uuin"
            },
            {
              "url": "url3",
              "club_id": "uuid",
              "image_id": "uuin"
            }
          ],
          "request_ids": [
            "uuid1",
            "uuid2",
            "uuid3"
          ]
       }

    """

    def __init__(self):
        pass


class ImageDto(BaseDto):
    """图片对应数据传输对象
    对应的json数据格式:
    {
        "url": "url1",
        "club_id": "uuid",
        "image_id": "uuid"
    }
    """
    def __init__(self):
        pass
