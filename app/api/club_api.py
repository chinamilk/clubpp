# -*-coding:utf-8-*-
"""Club api.

"""
import json
from datetime import date

from flask import request
from flask_restful import Resource

from app.api import ClubDto
from app.api.image_api import comvert_from_model_to_image_dto
from app.dao import Club
from app.dao import image_dao
from app.util import generate_uuid, str2date, add_attribute


class ClubsApi(Resource):
    def get(self) -> 'json':
        """对应 /api/clubs. 获取所有Club.

        """
        # club = Club()
        # club.club_id = "club1"
        # club.master_id = "1"
        # club.club_name = "chess"
        # club.member_number = 1
        # club_dao.add_club(club)
        # print(club_dao.get_club_by_id("club1").club_name)
        # club_dao.pass_club("club1")
        # print(club_dao.get_club_by_id("club1").is_passed)
        # return '{"resp": "hello"}'
        pass

    def post(self) -> 'json':
        """对应 /api/clubs. 新增一个Club.

        """
        print(json.loads(request.data.decode("utf-8")))
        pass


class ClubApi(Resource):
    def get(self, club_id: str) -> 'json':
        """对应 /api/clubs/<string:club_id>. 获取特定的Club.

        """
        pass

    def put(self, club_id: str) -> 'json':
        """对应 /api/clubs/<string:club_id>. 修改特定的Club.

        """
        pass

    def delete(self, club_id: str) -> 'json':
        """对应 /api/clubs/<string:club_id>. 删除特定的Club.

        """
        pass


def convert_from_model_to_dto(club: Club) -> ClubDto:
    """把Club对象转为需要的dto对象

    :param club:
    :return:
    """
    dto = ClubDto()
    dto.club_id = club.club_id
    dto.club_name = club.club_name
    dto.club_bio = club.club_bio
    dto.created_date = club.created_date.strftime('%Y-%m-%d')
    dto.member_number = club.member_number
    dto.master_id = club.master_id
    dto.tags = club.tags
    dto.addressed = club.addresses
    dto.images = map(comvert_from_model_to_image_dto, image_dao.get_images_by_club_id(club.club_id))
    # dto.request_ids = get_all_request_id_by_club_id()
    return dto


def convert_from_request_to_model(request: 'json') -> Club:
    """把请求中的json转为数据库操作需要的Club对象

    :param request: 请求中的json数据
    :return: 填充数据的Club对象
    """
    data = json.loads(request)
    return build_club(data.get("club_name"), data.get("club_bio"), data.get("member_number", -1), data.get("tags"),
                      data.get("addresses"), data.get("master_id"), str2date(data.get("created_date")))


def build_club(club_name: str = None, club_bio: str = None, member_number: int = -1, tags: str = None,
               addresses: str = None, master_id: str = None, created_date: date = None) -> Club:
    """Build club.

    :return: club instance
    """
    club = Club()
    club.club_id = generate_uuid()
    club.is_passed = False
    add_attribute(club, "club_name", club_name)
    add_attribute(club, "club_bio", club_bio)
    add_attribute(club, "member_number", member_number, default_value=-1)
    add_attribute(club, "tags", tags)
    add_attribute(club, "addresses", addresses)
    add_attribute(club, "master_id", master_id)
    add_attribute(club, "created_date", created_date)
    return club

# if __name__ == "__main__":
#     club = Club()
#     add_attribute(club, "at", "1", "1")
#     print(club.__dict__)
#     print(club.__dict__.get("hello"))
#     dtstr = "2018-1-2"
#     da = datetime.strptime(dtstr, "%Y-%m-%d").date()
#     print(da)
