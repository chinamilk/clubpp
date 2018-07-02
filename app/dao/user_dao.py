# -*-coding:utf-8-*-
from app import db
from app.dao import User, Request


def add_user(user: User):  # 测试通过
    db.session.add(user)
    db.session.commit()
    return User.query.get(user.user_id)


def update_user(user_id: 'str-要更新的用户id', user: User):  # 测试通过
    the_user = User.query.get(user_id)
    if isinstance(the_user, User):
        db.session.delete(the_user)
        db.session.add(user)
        db.session.commit()
        result = User.query.get(user_id)
    else:
        result = None
    return result


def get_user_by_username(u_name: str):  # 测试通过
    # user = User.query.filter_by(username=u_name).first()
    # if user is None:
    #     result = {'message': 'user ' + u_name + ' don\'t exist.'}
    # else:
    #     result = user
    # return result
    return User.query.filter_by(username=u_name).first()


def get_users():  # 测试通过
    result = User.query.all()
    return result


def get_user_by_id(user_id: int):  # 测试通过
    return User.query.filter_by(user_id=user_id).first()


def get_requests():
    return Request.query.all()
