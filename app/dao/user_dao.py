# -*-coding:utf-8-*-
from app import db
from app.dao import User
from app import util


def add_user(user: User):  # 测试通过
    db.session.add(user)
    db.session.commit()
    return User.query.get(user.user_id)


def update_user(user_id: 'str-要更新的用户id', user: User):  # 测试通过
    the_user = User.query.get(user_id)
    if isinstance(the_user, User):
        util.add_attribute(the_user, 'username', user.username)
        util.add_attribute(the_user, 'name', user.name)
        util.add_attribute(the_user, 'password', user.password)
        util.add_attribute(the_user, 'email', user.email)
        util.add_attribute(the_user, 'day_of_birth', user.day_of_birth)
        util.add_attribute(the_user, 'gender', user.gender)
        util.add_attribute(the_user, 'academy', user.academy)
        util.add_attribute(the_user, 'major', user.major)
        util.add_attribute(the_user, 'bio', user.bio)
        util.add_attribute(the_user, 'phone', user.phone)
        util.add_attribute(the_user, 'year_of_enrollment', user.year_of_enrollment)

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
