# -*-coding:utf-8-*-
from app import db
from app.dao import Request


def get_all_requests_by_club_id(club_id: str) -> list:
    """Get all requests by club id

    :param club_id: club id
    :return: list of requests
    """
    return db.session.query(Request).filter(Request.club_id == club_id).all()


def get_all_request_id_by_club_id(club_id: str) -> list:
    return db.session.query(Request.request_id).filter(Request.club_id == club_id).all()
