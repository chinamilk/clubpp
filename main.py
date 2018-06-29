# -*-coding:utf-8-*-
from flask_restful import Api

from app import create_app
from app.api.clubApi import ClubsApi
from app.api.imageApi import FileUploadApi
from app.api.userApi import HelloWorld

app = create_app()
api = Api(app)

api.add_resource(HelloWorld, '/<int:rate>', '/hello/<int:rate>')
api.add_resource(FileUploadApi, '/upload', endpoint="file_upload")

api.add_resource(ClubsApi, '/api/clubs')

if __name__ == '__main__':
    app.run(debug=True)
