from flask import request, render_template
from flask_restx import Namespace, Resource
from app.container import movie_service
from app.dao.models.movie import MovieSchema

movie_ns = Namespace("movies")

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MoviesView(Resource):
    def get(self):
        data = request.args
        items = movie_service.get_with_filter(data)
        results_json= movies_schema.dump(items)
        return results_json,200


@movie_ns.route("/<int:m_id>")
class MovieView(Resource):
    def get(self, m_id):
        result = movie_service.get_one(m_id)
        if result is not None:
            return movie_schema.dump(result), 200
        return "Записей с таким id нет в базе", 404
