# -*-coding:utf-8-*-
from flask import Flask
from flask_restful import Api

from app.api.imageApi import FileUploadApi
from app.api.userApi import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/<int:rate>', '/hello/<int:rate>')
api.add_resource(FileUploadApi, '/upload', endpoint="file_upload")

if __name__ == '__main__':
    app.run(debug=True)
