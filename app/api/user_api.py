# -*-coding:utf-8-*-
"""User
"""
import json

from flask_restful import Resource
from app.util import login_required, admin_required
from flask import request
from app.dao.user_dao import *
from app.dao.request_dao import get_requests
from app.dao import User
from app.util import generate_uuid
from app.util import obj2json
from app.util import BaseDto
from app import cors


class UsersDto(BaseDto):
    def __init__(self,
                 user_id='',
                 username='',
                 name='',
                 email='',
                 day_of_birth='',
                 gender='',
                 academy='',
                 major='',
                 bio='',
                 phone='',
                 year_of_enrollment='',
                 club_ids=None,
                 request_ids=None
                 ):
        self.user_id = user_id
        self.username = username
        self.name = name
        self.email = email
        self.day_of_birth = day_of_birth
        self.gender = gender
        self.academy = academy
        self.major = major
        self.bio = bio
        self.phone = phone
        self.year_of_enrollment = year_of_enrollment
        self.club_ids = club_ids
        self.request_ids = request_ids


def add_clubids_and_requestids_to_dto(user_result: User):
    requests_result = get_requests()
    club_ids = []
    request_ids = []
    for a_request in requests_result:
        if user_result.user_id == a_request.user_id:
            club_ids.append(a_request.club_id)
            request_ids.append(a_request.request_id)
    user_dto = UsersDto(
        user_id=user_result.user_id,
        username=user_result.username,
        name=user_result.name,
        email=user_result.email,
        day_of_birth=user_result.day_of_birth,
        gender=user_result.gender,
        academy=user_result.academy,
        major=user_result.major,
        bio=user_result.bio,
        phone=user_result.phone,
        year_of_enrollment=user_result.year_of_enrollment,
        club_ids=club_ids,
        request_ids=request_ids
    )
    return user_dto


class UsersApi(Resource):
    def post(self):  # 测试通过
        """对应 /api/users -post
        :param req: 添加的用户数据
        :return: 添加后的用户数据包括id
        """
        req = request.json
        user_result = add_user(User(
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
        user_dto = UsersDto(
            user_id=user_result.user_id,
            username=user_result.username,
            name=user_result.name,
            email=user_result.email,
            day_of_birth=user_result.day_of_birth,
            gender=user_result.gender,
            academy=user_result.academy,
            major=user_result.major,
            bio=user_result.bio,
            phone=user_result.phone,
            year_of_enrollment=user_result.year_of_enrollment,
            club_ids=[],
            request_ids=[]
        )
        res = user_dto

        return obj2json(res)

    def get(self):  # 测试通过
        '''
        根据是否有包含username的query_string判断返回一个用户or所有用户
        :return: 一个username相关用户or所有用户
        '''
        if request.query_string:
            query_str = str(request.query_string, encoding='utf-8')
            query_key_value = query_str.split('&')
            query_dict = {}
            for key_value in query_key_value:
                key, value = key_value.split('=')
                query_dict[key] = value

            if 'username' in query_dict.keys():
                user_result = get_user_by_username(query_dict['username'])
                if user_result is not None:
                    user_dto = add_clubids_and_requestids_to_dto(user_result)
                    res = user_dto
                else:
                    res = {'message': 'user ' + query_dict['username'] + ' don\'t exist.'}


class UsersApiById(Resource):
    @login_required
    def put(self, user_id):  # 测试通过
        """
        对应 /api/users/:user_id -put
        :param user_id: 将要被更新的用户id
        :return: 更新对应user_id的用户数据
        """
        req = request.json
        user_result = update_user(user_id, User(
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
        if user_result is not None:
            user_dto = add_clubids_and_requestids_to_dto(user_result)
            res = user_dto
        else:
            res = {'message': 'It\'s not exist that user you want update.'}
        return obj2json(res)

    @login_required
    def get(self, user_id):  # 测试通过
        """
        /api/users/:user_id -get
        根据id获取用户数据
        :param user_id: 用户id
        :return: 该id的用户数据
        """
        user = get_user_by_id(user_id)
        if user is None:
            res = {'message': 'user don\'t exist.'}
        else:
            user_result = user
            user_dto = add_clubids_and_requestids_to_dto(user_result)
            res = user_dto
        return obj2json(res)
