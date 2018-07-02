# -*-coding:utf-8-*-
import werkzeug
from flask_restful import Resource, reqparse

from app.api import ImageDto
from app.dao import Image
from app.util import map_path_to_url


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


class ImageApi(Resource):
    def post(self) -> 'json':
        """新增一张图片.
           对应URL为: /api/images

        :return: json
        """
        pass

    def delete(self) -> 'json':
        """删除一张图片.
           对应URL为: /api/images/<string: image_id>
        :return: json
        """
        pass


def comvert_from_model_to_image_dto(image: Image):
    """Convert from image to image dto

    :param image: image
    :return: image dto
    """
    dto = ImageDto()
    dto.url = map_path_to_url(image.image_path)
    dto.club_id = image.club_id
    dto.image_id = image.image_id
    return dto
