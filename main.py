# -*-coding:utf-8-*-
from flask_restful import Api

from app import create_app
from app.api.club_api import ClubsApi, ClubApi
from app.api.image_api import ImageApi
from app.api.request_api import RequestApi, RequestApiById
from app.api.user_api import UsersApi, UsersApiById

app = create_app()
api = Api(app)

# ZmfCn
# api.add_resource(FileUploadApi, '/upload', endpoint="file_upload")
api.add_resource(ClubsApi, '/api/clubs')
api.add_resource(ClubApi, '/api/clubs/<string:club_id>')
api.add_resource(ImageApi, '/api/images/<string:identifier>')

# cuppar
api.add_resource(UsersApi, '/api/users', '/api/users/')
api.add_resource(UsersApiById, '/api/users/<string:user_id>', '/api/users/<string:user_id>/')
api.add_resource(RequestApi, '/api/requests', '/api/requests/')
api.add_resource(RequestApiById, '/api/requests/<string:request_id>', '/api/requests/<string:request_id>/')


if __name__ == '__main__':
    app.run(debug=True)
