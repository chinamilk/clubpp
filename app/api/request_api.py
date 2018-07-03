# -*-coding:utf-8-*-
from app.util import BaseDto, generate_uuid
from flask_restful import Resource
from flask import request
import datetime
from app.dao.request_dao import *
from app.util import obj2json


class RequestDto(BaseDto):
    def __init__(self,
                 request_id=None,
                 user_id=None,
                 club_id=None,
                 time=None,
                 extra=None,
                 is_read=None
                 ):
        self.request_id = request_id
        self.user_id = user_id
        self.club_id = club_id
        self.time = time
        self.extra = extra
        self.is_read = is_read


class RequestApi(Resource):
    def post(self):  # 测试通过
        req = request.json
        request_result = add_request(Request(
            request_id=generate_uuid(),
            user_id=req.get('user_id'),
            club_id=req.get('club_id'),
            # time=time.time(),
            time=datetime.datetime.now(),
            extra=req.get('extra'),
            is_read=False
        ))
        request_dto = RequestDto(
            request_id=request_result.request_id,
            user_id=request_result.user_id,
            club_id=request_result.club_id,
            time=request_result.time,
            extra=request_result.extra,
            is_read=request_result.is_read,
        )
        res = request_dto
        return obj2json(res)

    def get(self):  # 测试通过
        requests_result = get_requests()
        request_dtos = []
        for a_request in requests_result:
            request_dto = RequestDto(
                request_id=a_request.request_id,
                user_id=a_request.user_id,
                club_id=a_request.club_id,
                time=a_request.time,
                extra=a_request.extra,
                is_read=a_request.is_read,
            )
            request_dtos.append(request_dto)
        res = request_dtos
        return obj2json(res)


class RequestApiById(Resource):
    def delete(self, request_id):  # 测试通过
        requests_result = get_requests()
        exist_the_request = False
        for a_request in requests_result:
            if a_request.request_id == request_id:
                exist_the_request = True
                break
        if exist_the_request:
            request_result = delete_request_by_id(request_id)
            request_dto = RequestDto(
                request_id=request_result.request_id,
                user_id=request_result.user_id,
                club_id=request_result.club_id,
                time=request_result.time,
                extra=request_result.extra,
                is_read=request_result.is_read,
            )
            res = request_dto
        else:
            res = {'message': 'the request ' + request_id + ' not exist.'}
        return obj2json(res)

    def get(self, request_id):  # 测试通过
        request_result = get_request_by_id(request_id)
        if request_result is None:
            res = {'message': 'request ' + request_id + ' is not exist.'}
        else:
            request_dto = RequestDto(
                request_id=request_result.request_id,
                user_id=request_result.user_id,
                club_id=request_result.club_id,
                time=request_result.time,
                extra=request_result.extra,
                is_read=request_result.is_read,
            )
            res = request_dto
        return obj2json(res)
