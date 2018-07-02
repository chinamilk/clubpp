# -*-coding:utf-8-*-
from flask_restful import Api

from app import create_app
from app.api.club_api import ClubsApi
from app.api.image_api import FileUploadApi
from app.api.user_api import UsersApi,UsersApiById

app = create_app()
api = Api(app)

api.add_resource(FileUploadApi, '/upload', endpoint="file_upload")

api.add_resource(ClubsApi, '/api/clubs')

# cuppar
api.add_resource(UsersApi, '/api/users', '/api/users/')
api.add_resource(UsersApiById, '/api/users/<string:user_id>', '/api/users/<string:user_id>/')


if __name__ == '__main__':
    app.run(debug=True)
