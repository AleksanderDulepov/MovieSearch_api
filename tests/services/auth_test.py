import pytest

from app.dao.models.user import User
from app.dao.user import UserDAO
from app.service.auth import UserService, AuthService
from unittest.mock import MagicMock


# отдельная фикстура user_dao для тестирвания методов auth_service
@pytest.fixture()
def user_dao():
    # создание подменного экземпляра дао, только для фикстуры
    user_dao = UserDAO(None)

    # подменные данные для тестирования без сервиса
    user_1 = User(id=1, email="alex@mail.ru", password="DFtqIBnTcCoXUp/NWRp+8L2yhrxRb1qboFR66MWjJ5k=")

    # переопределение методов
    user_dao.get_by_email = MagicMock(return_value=user_1)
    return user_dao


class TestAuthService:
    @pytest.fixture(autouse=True)
    def auth_service(self, user_dao):
        self.test_auth_service = AuthService(user_service=UserService(dao=user_dao))

    def test_generate_tokens(self):
        tokens = self.test_auth_service.generate_tokens(email="alex@mail.ru", password="1111111")
        assert tokens is not None, "Ошибка тестирования метода generate_tokens (возврат None значения)"
        assert {"access_token", "refresh_token"} == set(tokens.keys()), "Ошибка тестирования метода generate_tokens (" \
                                                                        "ключи)"
