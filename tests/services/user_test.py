import unittest

import pytest

from app.dao.models.genre import Genre
from app.dao.models.director import Director
from app.service.user import UserService


class TestUserService:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        self.test_user_service = UserService(dao=user_dao)

    def test_get_one(self):
        user = self.test_user_service.get_one(u_id=1)
        assert user is not None, "Ошибка тестирования метода get_one (возврат None значения)"
        assert user.id == 1, "Ошибка тестирования метода get_one (возврат обьекта с неверным id)"

    def test_get_by_email(self):
        user = self.test_user_service.get_by_email(email="Email_1")
        assert user is not None, "Ошибка тестирования метода get_by_email (возврат None значения)"
        assert user.email == "Email_1", "Ошибка тестирования метода get_by_email (возврат обьекта с неверным email)"

    def test_get_id_by_email(self):
        user_id = self.test_user_service.get_id_by_email(email="Email_1")
        assert user_id is not None, "Ошибка тестирования метода get_id_by_email (возврат None значения)"
        assert user_id == 1, "Ошибка тестирования метода get_id_by_email (возврат обьекта с неверным id)"

    def test_do_post(self):
        data = {"id": 4, "email": "Email_4", "password": "Password_user_4"}
        posted_user = self.test_user_service.do_post(data=data)
        assert posted_user is not None, "Ошибка тестирования метода do_post (возврат None значения)"
        assert posted_user.id == 4, "Ошибка тестирования метода do_post (возвращен неверный id)"

    def test_do_patch(self):
        data = {"name": "User_4"}
        patched_user = self.test_user_service.do_patch(email="Email_4", data=data)
        assert patched_user is not None, "Ошибка тестирования метода do_patch(возврат None значения)"
        assert patched_user.id == 4, "Ошибка тестирования метода do_patch (возвращен неверный id)"

    def test_make_user_password_hash(self):
        password = self.test_user_service.make_user_password_hash(password="1111111")
        assert password is not None, "Ошибка тестирования метода make_user_password_hash(возврат None значения)"
        assert password == b"DFtqIBnTcCoXUp/NWRp+8L2yhrxRb1qboFR66MWjJ5k=", "Ошибка тестирования метода " \
                                                                            "make_user_password_hash (неверный пароль)"

    def test_compare_password(self):
        is_matched = self.test_user_service.compare_password(
            hash_password_from_db="DFtqIBnTcCoXUp/NWRp+8L2yhrxRb1qboFR66MWjJ5k=", client_input_password="1111111")
        assert is_matched, "Ошибка тестирования метода compare_password (пароли не совпадают)"
