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
# SERVER_IP = "127.0.0.1"
BASIC_URL = "http://" + SERVER_IP + ":80"

DATETIME_PATTERN = '%Y-%m-%d %H:%M:%S'
DATE_PATTERN = "%Y-%m-%d"

SECRET_KEY = 'secret'

pymysql.install_as_MySQLdb()
db = SQLAlchemy()

cors = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "content-type, x-auth-token",
    "Access-Control-Allow-Methods": "GET, PUT, POST, DELETE, OPTIONS, HEAD",
}


def create_app():
    """factory method to create Flask instance

    :return: instance app
    """
    app = Flask(__name__)
    flask_cors.CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*",
                                                                       "methods": ["GET", "HEAD", "POST", "OPTIONS",
                                                                                   "PUT", "PATCH", "DELETE"],
                                                                       "allow_headers": "*"
                                                                       }})
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://clubpp:123456sql@localhost:3306/clubpp?charset=utf8mb4'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/clubpp?charset=utf8mb4'
    db.init_app(app)
    return app


app = create_app()
