# -*-coding:utf-8-*-
"""Club api.

"""
import json
from datetime import date

from flask import request, jsonify
from flask_restful import Resource

from app.api import ClubDto
from app.api import image_api
from app.dao import Club
from app.dao import club_dao
from app.dao import image_dao
from app.dao import request_dao
from app import util, DATE_PATTERN


class ClubsApi(Resource):
    # tested
    def get(self) -> 'json':
        """对应 /api/clubs. 获取所有Club.

        """
        clubs = club_dao.get_all_clubs()
        dtos = []
        for club in clubs:
            dtos.append(convert_from_model_to_dto(club))
        return util.obj2json(dtos)

    # tested
    def post(self) -> 'json':
        """对应 /api/clubs. 新增一个Club.

        """
        club = convert_from_request_to_model(request.data.decode("utf-8"))
        club_dao.add_club(club)
        club = club_dao.get_club_by_id(club.club_id)
        dto = convert_from_model_to_dto(club)
        return util.obj2json(dto)


class ClubApi(Resource):
    # tested
    def get(self, club_id: str) -> 'json':
        """对应 /api/clubs/<string:club_id>. 获取特定的Club.

        """
        club = club_dao.get_club_by_id(club_id)
        dto = convert_from_model_to_dto(club)
        return util.obj2json(dto)

    # tested
    def put(self, club_id: str) -> 'json':
        """对应 /api/clubs/<string:club_id>. 修改特定的Club.

        """
        club = convert_from_request_to_model(request.data.decode("utf-8"), club_id)
        print(club.club_name)
        club_dao.update_club(club)
        club = club_dao.get_club_by_id(club_id)
        dto = convert_from_model_to_dto(club)
        return util.obj2json(dto)

    # tested
    def delete(self, club_id: str) -> 'json':
        """对应 /api/clubs/<string:club_id>. 删除特定的Club.

        """
        club = club_dao.get_club_by_id(club_id)
        dto = convert_from_model_to_dto(club)
        club_dao.delete_club_by_id(club_id)
        return util.obj2json(dto)


def convert_from_model_to_dto(club: Club) -> ClubDto:
    """把Club对象转为需要的dto对象

    :param club:
    :return:
    """
    dto = ClubDto()
    dto.club_id = club.club_id
    dto.club_name = club.club_name
    dto.club_bio = club.club_bio
    dto.created_date = club.created_date.strftime(DATE_PATTERN) if club.created_date is not None else None
    dto.member_number = club.member_number
    dto.master_id = club.master_id
    dto.tags = club.tags
    dto.addressed = club.addresses
    dto.images = list(map(image_api.convert_from_model_to_image_dto, image_dao.get_images_by_club_id(club.club_id)))
    dto.request_ids = request_dao.get_all_request_id_by_club_id(club.club_id)
    return dto


def convert_from_request_to_model(req_body: 'json', club_id: str = util.generate_uuid()) -> Club:
    """把请求中的json转为数据库操作需要的Club对象

    :param req_body: 请求中的json数据
    :param club_id: 社团Id
    :return: 填充数据的Club对象
    """
    data = json.loads(req_body)
    date_str = data.get("created_date")
    created_date = util.str2date(date_str) if date_str is not None else None
    return build_club(data.get("club_name"), data.get("club_bio"), data.get("member_number", -1), data.get("tags"),
                      data.get("addresses"), data.get("master_id"), created_date, club_id)


def build_club(club_name: str = None, club_bio: str = None, member_number: int = -1, tags: str = None,
               addresses: str = None, master_id: str = None, created_date: date = None,
               club_id: str = util.generate_uuid()) -> Club:
    """Build club.

    :return: club instance
    """
    club = Club()
    club.club_id = club_id
    util.add_attribute(club, "club_name", club_name)
    util.add_attribute(club, "club_bio", club_bio)
    util.add_attribute(club, "member_number", member_number, default_value=-1)
    util.add_attribute(club, "tags", tags)
    util.add_attribute(club, "addresses", addresses)
    util.add_attribute(club, "master_id", master_id)
    util.add_attribute(club, "created_date", created_date)
    return club

# if __name__ == "__main__":
#     club = Club()
#     add_attribute(club, "at", "1", "1")
#     print(club.__dict__)
#     print(club.__dict__.get("hello"))
#     dtstr = "2018-1-2"
#     da = datetime.strptime(dtstr, "%Y-%m-%d").date()
#     print(da)
