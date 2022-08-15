import unittest

import pytest

from app.dao.models.genre import Genre
from app.dao.models.director import Director
from app.service.director import DirectorService


class TestDirectorService:
    @pytest.fixture(autouse=True)
    def director_service(self, director_dao):
        self.test_director_service = DirectorService(dao=director_dao)

    def test_get_one(self):
        director = self.test_director_service.get_one(d_id=1)
        assert director is not None, "Ошибка тестирования метода get_one (возврат None значения)"
        assert director.id == 1, "Ошибка тестирования метода get_one (возврат обьекта с неверным id)"

    def test_get_with_filter(self):
        director = self.test_director_service.get_all(data={"page": "1"})
        assert director is not None, "Ошибка тестирования метода get_all (возврат None значения)"
        assert isinstance(director, unittest.mock.Mock), "Ошибка тестирования метода get_all (возврат неверного " \
                                                         "значения)"
