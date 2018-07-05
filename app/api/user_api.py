# -*-coding:utf-8-*-
"""User

"""
from flask_restful import Resource
from app.util import login_required, admin_required


# example for restful
class HelloWorld(Resource):
    """each method is corresponding to a request method(GET, POST, PUT, DELETE)

    """

    @admin_required
    @login_required
    def get(self, rate):
        return {'hello': rate}

    def put(self, rate):
        return {'put': 'successful'}

    def post(self, rate):
        return {'post': 'successful'}

    def delete(self, rate):
        return {'delete': 'successful'}
