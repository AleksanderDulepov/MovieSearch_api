import pytest
from unittest.mock import MagicMock, Mock

from app.dao.bookmark import BookmarkDAO
from app.dao.director import DirectorDAO
from app.dao.genre import GenreDAO
from app.dao.models.bookmark import Bookmark
from app.dao.models.director import Director
from app.dao.models.genre import Genre
from app.dao.models.user import User
from app.dao.user import UserDAO
from main import configure_app, create_app

from app.config import Config_for_test
from app.dao.models.movie import Movie
from app.dao.movie import MovieDAO


# фикстуры с моками слоя DAO для тестирования сервисов

# movie
@pytest.fixture()
def movie_dao():
    # создание подменного экземпляра дао, только для фикстуры
    movie_dao = MovieDAO(None)
    # подменные данные для тестирования без сервиса
    movie_1 = Movie(id=1, title="Title_movie_1", description="Description_movie_1", year=2001)
    # переопределение методов
    mock = Mock()
    movie_dao.get_one = MagicMock(return_value=movie_1)
    movie_dao.get_with_filter = mock(return_value="It's work")

    return movie_dao


# genre
@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)
    genre_1 = Genre(id=1, name="Name_genre_1")
    genre_2 = Genre(id=2, name="Name_genre_2")
    # переопределение методов
    mock = Mock()
    genre_dao.get_one = MagicMock(return_value=genre_1)
    genre_dao.get_all = mock(return_value="It's work")

    return genre_dao


# director
@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)
    director_1 = Director(id=1, name="Name_director_1")
    director_2 = Director(id=2, name="Name_director_2")
    # переопределение методов
    mock = Mock()
    director_dao.get_one = MagicMock(return_value=director_1)
    director_dao.get_all = mock(return_value="It's work")

    return director_dao


# user
@pytest.fixture()
def user_dao():
    user_dao = UserDAO(None)
    user_1 = User(id=1, email="Email_1", password="Password_user_1")
    # переопределение методов
    user_dao.get_one = MagicMock(return_value=user_1)
    user_dao.get_by_email = MagicMock(return_value=user_1)
    user_dao.do_post = MagicMock(return_value=User(id=4))
    user_dao.do_update = MagicMock(return_value=User(id=4))
    return user_dao


# bookmark
@pytest.fixture()
def bookmark_dao():
    # создание подменного экземпляра дао, только для фикстуры
    bookmark_dao = BookmarkDAO(None)
    # подменные данные для тестирования без сервиса
    bookmark_1 = Bookmark(id=1, user_id=1, movie_id=1)
    # переопределение методов
    bookmark_dao.get_one = MagicMock(return_value=bookmark_1)
    bookmark_dao.do_post = MagicMock(return_value=bookmark_1)
    bookmark_dao.find_item_to_del = MagicMock(return_value=bookmark_1)
    bookmark_dao.do_delete = MagicMock(return_value=bookmark_1)

    return bookmark_dao


# #фикстура для тестирования вьюх

@pytest.fixture()
def app():
    app_config = Config_for_test()
    app = create_app(app_config)  # вызов функции создания и настройки приложения Flask
    configure_app(app)  # вызов функции конфигурирования приложения с БД, APi
    yield app


@pytest.fixture()
def test_client(app):
    return app.test_client()
