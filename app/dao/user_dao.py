# -*-coding:utf-8-*-
from app import db
from app.dao import User

def add_user(user: User):
    db.session.add(user)
    db.session.commit()

def update_user(user: User):
    pass

def get_user_by_name(username: str):
    pass

def get_users():
    pass

def get_user_by_id(user_id: int):
    pass