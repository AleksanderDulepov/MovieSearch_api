import calendar
import datetime

import jwt
from flask_restx import abort

from app.helper.constants import JWT_SECRET, JWT_ALGORITHM
from app.service.user import UserService


class AuthService():
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        user = self.user_service.get_by_email(email)  # экземпляр класса User из БД по email
        # если пользователя с email нет в БД:
        if user is None:
            abort(404, "Такого пользователя нет в базе")
        # если получаем новые токены, не по refresh(по refresh проверка пароля не требуется):
        if not is_refresh:
            is_correct_password = self.user_service.compare_password(user.password, password)
            # user.password-хеш из БД,password-чистый пароль от клиента
            if not is_correct_password:  # если пароли в виде хешей не совпали
                abort(400, "Передан неверный пароль")

        # если получаем и новые токены, и по refresh(без проверки пароля)
        # этот набор данных будет закодирован в токене
        data = {"email": user.email}

        # генерация access токена на 30 минут:
        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        # генерация refresh токена на 130 дней:
        day130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(day130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        return {"access_token": access_token, "refresh_token": refresh_token}

    def approve_refresh_token(self, refresh_token):
        try:
            data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
            email = data.get("email")
            return self.generate_tokens(email, None, is_refresh=True)
        except Exception as e:
            abort(400, "Переданный параметр refresh_token не валиден")
