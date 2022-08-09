from flask import request
from flask_restx import Namespace, Resource
from app.container import genre_sevice
from app.dao.models.genre import GenreSchema
from app.helper.utils import check_pagination

genre_ns = Namespace("genres")

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

#исправить пагинацию
@genre_ns.route("/")
class GenresView(Resource):
    def get(self):
        data = request.args
        results = genre_sevice.get_all(data)
        results_json= genres_schema.dump(results)
        return results_json,200



@genre_ns.route("/<int:g_id>")
class GenreView(Resource):
    def get(self, g_id):
        result = genre_sevice.get_one(g_id)
        if result is not None:
            return genre_schema.dump(result), 200
        return "Записей с таким id нет в базе", 404
