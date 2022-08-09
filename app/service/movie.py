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

        count_items = query.all()

        if data.get("page") is not None:
            page = int(data.get("page"))
            return query.paginate(page, AMOUNT_POSTS_PER_PAGE, False).items
        else:
            return query.paginate(1, len(count_items), False).items
