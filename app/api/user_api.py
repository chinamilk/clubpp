# -*-coding:utf-8-*-
"""User

"""
from flask_restful import Resource
from flask import request
import json

class UsersApi(Resource):
    def post(self):
        '''对应 /api/users -post

        :param req: 添加的用户数据
        :return: 添加后的用户数据包括id
        '''
        req=request.json
        return {'/api/users': req}
    def put(self, user_id):
        '''
        对应 /api/users/:user_id -put
        :param user: 更新的用户数据
        :return: 更新对应user_id的用户数据
        '''
        req=request.form['foo']
        return {'/api/users/:user_id -put': 'successful',
                'user_id': user_id,
                'req': req
                }
    def get(self):
        '''
        根据是否有username的query_string判断返回一个用户or所有用户
        :return: 一个username相关用户or所有用户
        '''
        if request.query_string:
            results={
                'username': str(request.query_string, encoding='utf-8')
            }
        else:
            results={
                'all': '[users]'
            }
        return results

class UsersApiGetById(Resource):
    def get(self, user_id):
        '''
        /api/users/:user_id -get
        根据id获取用户数据
        :param user_id: 用户id
        :return: 该id的用户数据
        '''
        return {
            '/api/users/:user_id -get': 'successful',
            'user_id': user_id
        }

# class UsersApiGetByName(Resource):
#     def get(self):
#         '''
#         /api/users?name=cuppar -get
#         根据用户名获取用户数据
#         :param username: 用户名
#         :return: 该用户名的用户数据
#         '''
#         username=request.query_string.username
#         return {
#             '/api/users?name=cuppar -get': 'userMsg',
#             'username': username
#         }
#
# class UsersApiGetAll(Resource):
#     def get(self):
#         '''
#         /api/users -get
#         获取所有用户
#         :return: 所有用户数据（列表）
#         '''
#         return {
#             '/api/users -get': '[msgs]'
#         }
