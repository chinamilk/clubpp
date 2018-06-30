# -*-coding:utf-8-*-
"""User

"""
from flask_restful import Resource

class UsersApi(Resource):
    def post(self, req):
        '''对应 /api/users

        :param req: 添加的用户数据
        :return: 添加后的用户数据包括id
        '''
        pass

    def put(self, user_id, req):
        '''
        对应 /api/users/:user_id
        :param user: 更新的用户数据
        :return: 更新对应user_id的用户数据
        '''
        pass




# example for restful
class HelloWorld(Resource):
    """each method is corresponding to a request method(GET, POST, PUT, DELETE)

    """
    def get(self, rate):
        return {'hello': rate}

    def put(self):
        return {'put': 'successful'}

    def post(self):
        return {'post': 'successful'}

    def delete(self):
        return {'delete': 'successful'}