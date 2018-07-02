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
    db.session.add(club)
    db.session.commit()


def get_club_by_id(club_id: str) -> Club:
    """Get club instance by club id.

    :param club_id: club id
    :return: club instance
    """
    return db.session.query(Club).filter(Club.club_id == club_id).first()


def update_club(club: Club):
    """Update a club in the database.

    :param club: the club instance with data and club id
    :return: None
    """
    record = db.session.query(Club).filter(Club.club_id == club.club_id).first()
    record.club_name = club.club_name
    record.member_number = club.member_number
    record.club_bio = club.club_bio
    record.master_id = club.master_id
    record.tags = club.tags
    record.addresses = club.addresses
    record.created_date = club.created_date
    db.session.commit()


def pass_club(club_id: str):
    """Pass the establishment of the club.

    :param club_id: the club id
    :return: None
    """
    record = db.session.query(Club).filter(Club.club_id == club_id).first()
    record.is_passed = True
    db.session.commit()


def delete_club_by_id(club_id: str):
    """Delete club by id.

    :param club_id: club id
    :return: None
    """
    record = db.session.query(Club).filter(Club.club_id == club_id).first()
    db.session.delete(record)
    db.session.commit()


def get_all_clubs() -> list:
    """Get all clubs whose if_passed is True in database.

    :return: a list that contains all clubs
    """
    return db.session.query(Club).filter(Club.is_passed == True).first()
