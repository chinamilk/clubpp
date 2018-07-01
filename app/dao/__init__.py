# -*-coding:utf-8-*-
"""dao包包含对数据库的操作，可以将对数据库的操作写成CRUD的API给api包中的函数调用

"""
from app import db


class User(db.Model):
    """Model for clubpp.user

    """
    __tablename__ = "user"
    user_id = db.Column(db.VARCHAR, primary_key=True)
    username = db.Column(db.VARCHAR, unique=True, nullable=False)
    email = db.Column(db.VARCHAR, nullable=False)
    day_of_birth = db.Column(db.DATE, nullable=False)
    password = db.Column(db.VARCHAR, nullable=False)
    gender = db.Column(db.Boolean, nullable=False)
    academy = db.Column(db.VARCHAR, nullable=False)
    major = db.Column(db.VARCHAR, nullable=False)
    avatar_path = db.Column(db.VARCHAR, nullable=False)
    phone = db.Column(db.VARCHAR, nullable=False)
    name = db.Column(db.VARCHAR, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)
    year_of_enrollment = db.Column(db.Integer, nullable=False)

    def __init__(self,
                 user_id,
                 username,
                 name,
                 password,
                 email,
                 day_of_birth,
                 gender,
                 academy,
                 major,
                 bio,
                 phone,
                 year_of_enrollment
                 ):
        self.user_id = user_id
        self.username = username
        self.name = name
        self.password = password
        self.email = email
        self.day_of_birth = day_of_birth
        self.gender = gender
        self.academy = academy
        self.major = major
        self.bio = bio
        self.phone = phone
        self.year_of_enrollment = year_of_enrollment

    def __repr__(self):
        return '<User %r>' % self.username


class Club(db.Model):
    """Model for clubpp.club

    """
    __tablename__ = "club"
    club_id = db.Column(db.VARCHAR, primary_key=True)
    club_name = db.Column(db.VARCHAR, nullable=False)
    create_date = db.Column(db.DATE, nullable=False)
    member_number = db.Column(db.Integer, nullable=False)
    club_bio = db.Column(db.VARCHAR, nullable=False)
    tags = db.Column(db.VARCHAR, nullable=False)
    addresses = db.Column(db.VARCHAR, nullable=False)
    master_id = db.Column(db.VARCHAR, db.ForeignKey('user.user_id'), nullable=False)
    is_passed = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<Club %r>' % self.name


class Request(db.Model):
    """Model for clubpp.request

    """
    __tablename__ = "request"
    request_id = db.Column(db.VARCHAR, primary_key=True)
    user_id = db.Column(db.VARCHAR, db.ForeignKey('user.user_id'), nullable=False)
    club_id = db.Column(db.VARCHAR, db.ForeignKey('club.club_id'), nullable=False)
    time = db.Column(db.TIMESTAMP, nullable=False)
    extra = db.Column(db.VARCHAR, nullable=False)
    is_read = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return '<Request %r>' % self.request_id


class Image(db.Model):
    """Model for clubpp.image

    """
    __tablename__ = "image"
    image_id = db.Column(db.VARCHAR, primary_key=True)
    image_path = db.Column(db.VARCHAR, nullable=False)
    club_id = db.Column(db.VARCHAR, db.ForeignKey('club.club_id'), nullable=False)

    def __repr__(self):
        return '<Image %r>' % self.image_id
