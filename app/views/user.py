from flask import request
from flask_restx import Namespace, Resource
from app.container import user_service
from app.dao.models.user import UserSchema
from app.helper.decorators import auth_only

user_ns = Namespace("users")

user_schema = UserSchema()


@user_ns.route("/")
class UserView(Resource):
    @auth_only
    def get(self, email_from_decorator=None):
        result = user_service.get_by_email(email_from_decorator)
        return user_schema.dump(result), 200

    @auth_only
    def patch(self, email_from_decorator=None):
        data = request.json
        result = user_service.do_patch(email_from_decorator, data)
        if result is not None:
            return "", 204
        return "Запись не была обновлена", 405


@user_ns.route("/password")
class UserPassView(Resource):
    @auth_only
    def put(self, email_from_decorator=None):
        data = request.json
        result = user_service.do_put(email_from_decorator, data)
        if result is not None:
            return "", 204
        return "Запись не была обновлена", 405
