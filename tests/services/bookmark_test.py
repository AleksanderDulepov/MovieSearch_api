import unittest

import pytest

from app.dao.models.genre import Genre
from app.dao.models.director import Director
from app.service.bookmark import BookmarkService
from app.service.user import UserService


class TestBookmarkService:
    @pytest.fixture(autouse=True)
    def bookmark_service(self, bookmark_dao, user_dao):
        self.test_bookmark_service = BookmarkService(bookmark_dao=bookmark_dao, user_service=UserService(dao=user_dao))

    def test_do_post(self):
        bookmark = self.test_bookmark_service.do_post(m_id=1, email="Email_1")
        assert bookmark is not None, "Ошибка тестирования метода do_post (возврат None значения)"
        assert bookmark.id == 1, "Ошибка тестирования метода do_post (возврат обьекта с неверным id)"

    def test_get_with_filter(self):
        bookmark = self.test_bookmark_service.delete_one(m_id=1, email="Email_1")
        assert bookmark is not None, "Ошибка тестирования метода delete_one (возврат None значения)"
        assert bookmark.id == 1, "Ошибка тестирования метода delete_one (возврат обьекта с неверным id)"
