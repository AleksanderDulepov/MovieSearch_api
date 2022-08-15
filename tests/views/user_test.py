from unittest import mock


class TestUser:

    def test_user_view_not_allowed(self, test_client):
        headers_to_test = {"Autorization": "Bearer XXX"}
        response = test_client.get("/users/", headers=headers_to_test)
        assert response.status_code == 401, "Некорректная работа декоратора auth_only"

    @mock.patch('app.helper.decorators.check_valid', mock.MagicMock(return_value="alex@mail.ru"))
    def test_user_view_allowed(self, test_client):
        keys_should_be = {"id", "email", "password", "name", "surname", "favorite_genre"}
        response = test_client.get("/users/")
        assert response.status_code == 200, "Некорректный статус-код ответа для эндпоинта get('/users/')"
        assert response.json["name"] == "Alex", "Некорректный ответ для эндпоинта get('/users/')"
        assert len(response.json) == 6, "Некорректное количество ключей ответа для эндпоинта get('/users/')"
        assert keys_should_be == set(response.json.keys()), "Некорректные ключи ответа для эндпоинта get('/users/')"

    @mock.patch('app.helper.decorators.check_valid', mock.MagicMock(return_value="alex@mail.ru"))
    def test_user_patch(self, test_client):
        response = test_client.patch("/users/", json={"favorite_genre": 8})
        assert response.status_code == 204, "Некорректный статус-код ответа для эндпоинта patch('/users/')"

    # @mock.patch('app.helper.decorators.check_valid', mock.MagicMock(return_value="alex@mail.ru"))
    # def test_user_put(self, test_client):
    #     response = test_client.put("/users/",json={"password_1":"1111111", "password_2":"1111"})
    #     assert response.status_code ==204, "Некорректный статус-код ответа для эндпоинта put('/users/password')"
