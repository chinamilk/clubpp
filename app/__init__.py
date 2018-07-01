# -*-coding:utf-8-*-
"""校园社团招新平台

"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()
db = SQLAlchemy()


def create_app():
    """factory method to create Flask instance

    :return: instance app
    """
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/clubpp?charset=utf8mb4'
    db.init_app(app)
    return app
