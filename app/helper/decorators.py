import jwt
from flask import request
from flask_restx import abort

from app.helper.constants import JWT_SECRET, JWT_ALGORITHM


def auth_only(func):
    def wrapper(*args, **kwargs):
        # проверка наличия заголовка в запросе
        if "Authorization" not in request.headers:
            abort(401, "Не передан токен")

        data = request.headers["Authorization"]
        token = data.split("Bearer ")[-1]  # вычленение самого токена из заголовка

        try:
            user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            # извлечение email из payload части раскодированного токена
            email = user.get("email")
        except Exception as e:
            abort(401, "Передан не валидный токен")
        return func(*args, **kwargs, email_from_decorator=email)

    return wrapper
