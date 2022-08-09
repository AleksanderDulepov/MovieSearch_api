from flask import request
from flask_restx import Namespace, Resource
from app.container import auth_service
from app.container import user_service

auth_ns = Namespace("auth")


@auth_ns.route("/register")
class RegView(Resource):
    def post(self):  # регистрация userов в БД
        data = request.json
        results = user_service.do_post(data)
        if results is not None:
            return "", 201
        return "Запись не была добавлена", 405


@auth_ns.route("/login")
class AuthView(Resource):
    def post(self):  # получение токенов при авторизации
        data = request.json
        email = data.get("email", None)
        password = data.get("password", None)
        if None in [email, password]:
            return "", 400
        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201

    def put(self):  # получение токенов по refresh токену
        data = request.json
        token = data.get('refresh_token')
        tokens = auth_service.approve_refresh_token(token)
        return tokens, 201
