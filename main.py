# -*-coding:utf-8-*-
from flask_restful import Api

from app import create_app
from app.api.club_api import ClubsApi, ClubApi
from app.api.image_api import ClubImageApi
from app.api.request_api import RequestApi, RequestApiById
from app.api.user_api import UsersApi, UsersApiById

from app.dao import user_dao, User

from flask import request, make_response, jsonify

app = create_app()
api = Api(app)

# ZmfCn
# api.add_resource(FileUploadApi, '/upload', endpoint="file_upload")
api.add_resource(ClubsApi, '/api/clubs')
api.add_resource(ClubApi, '/api/clubs/<string:club_id>')
api.add_resource(ClubImageApi, '/api/images/<string:identifier>')

# cuppar
api.add_resource(UsersApi, '/api/users', '/api/users/')
api.add_resource(UsersApiById, '/api/users/<string:user_id>', '/api/users/<string:user_id>/')
api.add_resource(RequestApi, '/api/requests', '/api/requests/')
api.add_resource(RequestApiById, '/api/requests/<string:request_id>', '/api/requests/<string:request_id>/')


@app.route('/login', methods=['POST'])
def my_login():
    request_data_dict = eval(str(request.data, encoding="utf8").replace('\n', '').replace('\t', ''))
    username = request_data_dict['username']
    data = user_dao.if_username_exist(username)

    # 用户名不存在
    if len(data) == 0:
        return make_response('用户名不存在！', 400)

    # 验证密码
    if not request_data_dict['password'] == user_dao.get_password_by_username(username)[0][0]:
        return make_response('密码错误！', 400)

    user = User()
    token = str(user.jwt_encoding(), encoding="utf8")

    token_json = {'token': token}

    return jsonify(token_json)


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', port='5005')
