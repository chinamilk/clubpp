# -*-coding:utf-8-*-
"""校园社团招新平台

"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import flask_cors

DESTINATION_DIR = "/var/www/html/download/clubpp/"
WWW_ROOT = "/var/www/html"
SERVER_IP = "120.78.187.115"
BASIC_URL = "http://" + SERVER_IP + ":80"

DATETIME_PATTERN = '%Y-%m-%d %H:%M:%S'
DATE_PATTERN = "%Y-%m-%d"

pymysql.install_as_MySQLdb()
db = SQLAlchemy()


def create_app():
    """factory method to create Flask instance

    :return: instance app
    """
    app = Flask(__name__)
    flask_cors.CORS(app, supports_credentials=True)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/clubpp?charset=utf8mb4'
    db.init_app(app)
    return app
