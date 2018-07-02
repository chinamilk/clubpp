# -*-coding:utf-8-*-
from app.dao import Request
from app import db


def get_requests():
    return Request.query.all()


def add_request(request: Request):
    db.session.add(request)
    db.session.commit()
    return Request.query.get(request.request_id)


def delete_request_by_id(request_id):
    deleted_request = Request.query.get(request_id)
    db.session.delete(deleted_request)
    db.session.commit()
    return deleted_request


def get_request_by_id(request_id):
    return Request.query.get(request_id)
