# -*-coding:utf-8-*-
"""User

"""
from flask_restful import Resource


# example for restful
class HelloWorld(Resource):
    """each method is corresponding to a request method(GET, POST, PUT, DELETE)

    """

    def get(self, rate):
        return {'hello': rate}

    def put(self, rate):
        return {'put': 'successful'}

    def post(self, rate):
        return {'post': 'successful'}

    def delete(self, rate):
        return {'delete': 'successful'}
