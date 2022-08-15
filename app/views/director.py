from flask import request
from flask_restx import Namespace, Resource
from app.container import director_sevice
from app.dao.models.director import DirectorSchema
from app.helper.constants import AMOUNT_POSTS_PER_PAGE


director_ns = Namespace("directors")

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

#исправить пагинацию
@director_ns.route("/")
class DirectorsView(Resource):
    def get(self):
        data = request.args
        results = director_sevice.get_all(data)
        results_json = directors_schema.dump(results)
        return results_json, 200




@director_ns.route("/<int:d_id>")
class DirectorView(Resource):
    def get(self, d_id):
        result = director_sevice.get_one(d_id)
        if result is not None:
            return director_schema.dump(result), 200
        return "Записей с таким id нет в базе", 404
