# -*-coding:utf-8-*-
from app import db
from app.dao import Request


def get_all_requests_by_club_id(club_id: str) -> list:
    """Get all requests by club id

    :param club_id: club id
    :return: list of requests
    """
    return db.session.query(Request).filter(Request.club_id == club_id).all()

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

