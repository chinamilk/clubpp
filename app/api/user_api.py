# -*-coding:utf-8-*-
"""User

"""
from flask_restful import Resource
from flask import request
from app.dao.user_dao import *
from app.dao import User
from app.util import generate_uuid
from app.util import obj2json


class UsersApi(Resource):
    def post(self):  # 测试通过
        '''对应 /api/users -post

        :param req: 添加的用户数据
        :return: 添加后的用户数据包括id
        '''
        req = request.json
        result = add_user(User(
            generate_uuid(),
            req.get('username'),
            req.get('name'),
            req.get('password'),
            req.get('email'),
            req.get('day_of_birth'),
            req.get('gender'),
            req.get('academy'),
            req.get('major'),
            req.get('bio'),
            req.get('phone'),
            req.get('year_of_enrollment')
        ))
        return str(result)

    def get(self):  # 测试通过
        '''
        根据是否有包含username的query_string判断返回一个用户or所有用户
        :return: 一个username相关用户or所有用户
        '''
        if request.query_string:
            # result={'query_string': str(request.query_string, encoding='utf-8')}
            query_str = str(request.query_string, encoding='utf-8')
            query_key_value = query_str.split('&')
            query_dict = {}
            for key_value in query_key_value:
                key, value = key_value.split('=')
                query_dict[key] = value

            if 'username' in query_dict.keys():
                result = get_user_by_username(query_dict['username'])
            else:
                result = {
                    'message': 'query_string don\'t have the "username" property.'
                }
        else:
            result = get_users()
        return str(result)


class UsersApiById(Resource):
    def put(self, user_id):  # 测试通过
        '''
        对应 /api/users/:user_id -put
        :param user: 更新的用户数据
        :return: 更新对应user_id的用户数据
        '''
        req = request.json
        result = update_user(user_id, User(
            user_id,
            req.get('username'),
            req.get('name'),
            req.get('password'),
            req.get('email'),
            req.get('day_of_birth'),
            req.get('gender'),
            req.get('academy'),
            req.get('major'),
            req.get('bio'),
            req.get('phone'),
            req.get('year_of_enrollment')
        ))

        # return obj2json(result)
        return str(result)

    def get(self, user_id):  # 测试通过
        '''
        /api/users/:user_id -get
        根据id获取用户数据
        :param user_id: 用户id
        :return: 该id的用户数据
        '''
        user = get_user_by_id(user_id)
        if user is None:
            result = {'message': 'user don\'t exist.'}
        else:
            result = user
        return str(result)

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
