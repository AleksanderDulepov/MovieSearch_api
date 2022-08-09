from flask_restx import Namespace, Resource
from app.container import bookmark_service, movie_service
from app.dao.models.bookmark import BookmarkSchema
from app.helper.decorators import auth_only

bookmark_ns = Namespace("favorites")

bookmark_schema = BookmarkSchema()
bookmarks_schema = BookmarkSchema(many=True)


@bookmark_ns.route("/movies/<int:m_id>")
class BookmarksView(Resource):
    @auth_only
    def post(self, m_id, email_from_decorator=None):
        # проверка существования фильма с m_id в базе
        if movie_service.get_one(m_id=m_id) is None:
            return "Фильмов с таким id нет в базе", 404
        results = bookmark_service.do_post(m_id, email_from_decorator)
        if results is not None:
            return "", 201
        return "Запись не была добавлена", 405

    @auth_only
    def delete(self, m_id, email_from_decorator=None):
        results = bookmark_service.delete_one(m_id, email_from_decorator)
        if results is not None:
            return "", 204
        return "Запись не была удалена", 404
