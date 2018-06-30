# -*-coding:utf-8-*-
"""Database operations about table image.

"""

from . import Image


def get_image_by_id(image_id: str) -> Image:
    """Get image by image_id

    :param image_id: image id
    :return: image instance
    """
    pass


def get_images_by_club_id(club_id: str) -> list:
    """Get images by club_id

    :param club_id: club_id
    :return: list that contains all images of the club
    """
    pass


def add_image(image: Image):
    """Add image to the database

    :param image: image instance that contains all data
    :return: None
    """
    pass


def delete_image_by_id(image_id: str):
    """Delete image by image_id

    :param image_id: image id
    :return: None
    """
    pass
