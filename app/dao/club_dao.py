# -*-coding:utf-8-*-
"""Database operations about table club.

"""
from app import db
from app.dao import Club


def add_club(club: Club):
    """Add a club to the database.

    :param club: the club instance with data
    :return: None
    """
    pass


def get_club_by_id(club_id: str) -> Club:
    """Get club instance by club id.

    :param club_id: club id
    :return: club instance
    """
    return db.session.query(Club).filter(Club.addresses == " ").first()
    pass


def update_club(club: Club):
    """Update a club in the database.

    :param club: the club instance with data and club id
    :return: None
    """
    pass


def delete_club_by_id(club_id: str):
    """Delete club by id.

    :param club_id: club id
    :return: None
    """
    pass


def get_all_clubs() -> list:
    """Get all clubs in database.

    :return: a list that contains all clubs
    """
    pass
