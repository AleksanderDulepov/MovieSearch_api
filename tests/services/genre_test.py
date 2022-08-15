import unittest

import pytest

from app.dao.models.genre import Genre
from app.dao.models.director import Director
from app.service.genre import GenreService


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.test_genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.test_genre_service.get_one(g_id=1)
        assert genre is not None, "Ошибка тестирования метода get_one (возврат None значения)"
        assert genre.id == 1, "Ошибка тестирования метода get_one (возврат обьекта с неверным id)"

    def test_get_with_filter(self):
        genre = self.test_genre_service.get_all(data={"page": "1"})
        assert genre is not None, "Ошибка тестирования метода get_all (возврат None значения)"
        assert isinstance(genre, unittest.mock.Mock), "Ошибка тестирования метода get_all (возврат неверного " \
                                                      "значения)"
