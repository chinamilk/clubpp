# -*-coding:utf-8-*-
import mysql.connector

from app import db, util
from app.dao import User


class ContextManagement:
    def __init__(self, config: dict) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()


databaseConfig = {'host': 'localhost',
                  'user': 'root',
                  'passwd': '',
                  'db': 'clubpp'}


def if_username_exist(username):
    with ContextManagement(databaseConfig) as cursor:
        cursor.execute("select * from user where username = '%s'" % username)
        data = cursor.fetchall()
        return data


def get_user_id_by_username(username: str):
    """

    :return:
    """
    return 'gfn'


def get_is_admin_by_username(username: str):
    """

    :param username:
    :return:
    """
    with ContextManagement(databaseConfig) as cursor:
        cursor.execute("select is_admin from user where username = '%s'" % username)
        data = cursor.fetchall()
        return data


def get_password_by_username(username: str):
    """

    :param username:
    :return:
    """
    with ContextManagement(databaseConfig) as cursor:
        cursor.execute("select password from user where username = '%s'" % username)
        data = cursor.fetchall()
        return data


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
