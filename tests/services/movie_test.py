import unittest

import pytest

from app.dao.models.genre import Genre
from app.dao.models.director import Director
from app.service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.test_movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.test_movie_service.get_one(m_id=1)
        assert movie is not None, "Ошибка тестирования метода get_one (возврат None значения)"
        assert movie.id == 1, "Ошибка тестирования метода get_one (возврат обьекта с неверным id)"

    def test_get_with_filter(self):
        movie = self.test_movie_service.get_with_filter(data={"status": "new", "page": "1"})
        assert movie is not None, "Ошибка тестирования метода get_with_filter (возврат None значения)"
        assert isinstance(movie, unittest.mock.Mock), "Ошибка тестирования метода get_with_filter (возврат неверного " \
                                                      "значения)"
