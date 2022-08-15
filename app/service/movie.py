from app.dao.models.movie import Movie
from app.helper.constants import AMOUNT_POSTS_PER_PAGE


class MovieService:
    def __init__(self, dao):
        self.dao = dao

    def get_one(self, m_id):
        return self.dao.get_one(m_id)

    def get_with_filter(self, data):
        status = data.get("status")
        if status == "new":
            query = self.dao.get_with_filter(True)
        else:
            query = self.dao.get_with_filter()

        if data.get("page") is not None:
            page = int(data.get("page"))
            return query.paginate(page=page, per_page=AMOUNT_POSTS_PER_PAGE, error_out=False).items
        else:
            count_items = query.all()
            return query.paginate(1, len(count_items), False).items
