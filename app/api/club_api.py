# -*-coding:utf-8-*-
"""Club api.

"""
from flask_restful import Resource

from app.dao import club_dao


class ClubDto:
    """club接口数据传输对象.

    """

    def __init__(self):
        pass


class ClubsApi(Resource):
    def get(self) -> 'json':
        """对应 /api/clubs. 获取所有Club.

        """
        # user = User()
        # user.username = "zmf"
        # user.user_id = "1"
        # user.gender = False
        # add_user(user)
        print(club_dao.get_club_by_id("1").user_id)
        pass

    def post(self) -> 'json':
        """对应 /api/clubs. 新增一个Club.

        """
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
