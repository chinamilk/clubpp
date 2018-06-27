import werkzeug
from flask_restful import Resource, reqparse


class FileUploadApi(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files')
        args = parser.parse_args()
        file = args.get('image')
        print("image", file)
        print(args)
        file.save("/home/zmf/Documents/aaaaaaaaaaaaaaaaaaaaa.png")
        return {'post': 'successful'}