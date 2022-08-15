import random


class TestAuth:

    def test_view_auth_register_post(self, test_client):
        response = test_client.post("/auth/register", json={"email": f'Test_email{random.randint(0, 10000)}',
                                                            "password": "0000",
                                                            "name": "Test_name", "surname": "Test_surname",
                                                            "favorite_genre": "1"})
        assert response.status_code == 201, "Некорректный статус-код ответа для эндпоинта post('/auth/register')"

    def test_view_auth_login_post(self, test_client):
        keys_should_be = {"access_token", "refresh_token"}
        response = test_client.post("/auth/login", json={"email": "alex@mail.ru", 'password': '1111111'})
        assert response.status_code == 201, "Некорректный статус-код ответа для эндпоинта post('/auth/login')"
        assert keys_should_be == set(
            response.json.keys()), "Некорректные ключи ответа для эндпоинта post('/auth/login')"
