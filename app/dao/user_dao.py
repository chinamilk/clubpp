# -*-coding:utf-8-*-
import mysql.connector

class ContextManagement:
    def __init__(self, config:dict) -> None:
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

def get_user_id_by_username(username:str):
    """

    :return:
    """
    return 'gfn'


def get_is_admin_by_username(username:str):
    """

    :param username:
    :return:
    """
    with ContextManagement(databaseConfig) as cursor:
        cursor.execute("select is_admin from user where username = '%s'" % username)
        data = cursor.fetchall()
        return data


def get_password_by_username(username:str):
    """

    :param username:
    :return:
    """
    with ContextManagement(databaseConfig) as cursor:
        cursor.execute("select password from user where username = '%s'" % username)
        data = cursor.fetchall()
        return data

