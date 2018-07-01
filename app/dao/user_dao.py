# -*-coding:utf-8-*-
from app import db
from app.dao import User


def add_user(user: User):  # 测试通过
    db.session.add(user)
    db.session.commit()
    return User.query.get(user.user_id)


def update_user(user_id: 'str-要更新的用户id', user: User):  # 测试通过
    if User.query.get(user_id) == None:
        result = {'message': 'It\'s not exist that user you want update.'}
    else:
        db.session.delete(User.query.get(user_id))
        # db.session.commit()
        db.session.add(user)
        db.session.commit()
        result = User.query.get(user_id)
    return result


# return User.query.get(user.user_id)
# return User.query.all()


def get_user_by_username(uname: str):  # 测试通过
    user = User.query.filter_by(username=uname).first()
    if user is None:
        result = {'message': 'user ' + uname + ' don\'t exist.'}
    else:
        result = user
    return str(result)


def get_users():  # 测试通过
    result = User.query.all()
    return result


def get_user_by_id(user_id: int):  # 测试通过
    return User.query.filter_by(user_id=user_id).first()
