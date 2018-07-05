# -*-coding:utf-8-*-
import werkzeug
from flask_restful import Resource, reqparse

from app import DESTINATION_DIR
from app import util
from app.api import ImageDto
from app.dao import Image, image_dao
from app.util import login_required


class ImageApi(Resource):
    # tested
    @login_required
    def post(self, identifier) -> 'json':
        """新增一张图片.
           对应URL为: /api/images/<string: identifier>

        :return: json
        """
        parser = reqparse.RequestParser()
        parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files', required=True,
                            help="图片不能为空")
        args = parser.parse_args()
        file = args.get('file')
        image = build_image(identifier, file.filename)
        file.save(image.image_path)
        image_dao.add_image(image)
        image = image_dao.get_image_by_id(image.image_id)
        dto = convert_from_model_to_image_dto(image)
        return util.obj2json(dto)

    # tested
    @login_required
    def delete(self, identifier) -> 'json':
        """删除一张图片.
           对应URL为: /api/images/<string: identifier>
        :return: json
        """
        image = image_dao.get_image_by_id(identifier)
        image_dao.delete_image_by_id(identifier)
        dto = convert_from_model_to_image_dto(image)
        return util.obj2json(dto)


def convert_from_model_to_image_dto(image: Image):
    """Convert from image to image dto

    :param image: image
    :return: image dto
    """
    dto = ImageDto()
    dto.url = util.map_path_to_url(image.image_path)
    dto.club_id = image.club_id
    dto.image_id = image.image_id
    return dto


def build_image(club_id: str, origin_name: str) -> Image:
    """Build a new image according to the club id.

    :param club_id: the id of the club that owns the image.
    :param origin_name: the origin name of the image.
    :return: the instance of Image.
    """
    image = Image()
    image.club_id = club_id
    suffix = origin_name.split('.')[-1]
    image.image_id = util.generate_uuid()
    image_name = image.image_id + '.' + suffix
    image.image_path = DESTINATION_DIR + image_name
    return image
