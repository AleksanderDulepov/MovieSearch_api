from app.helper.constants import AMOUNT_POSTS_PER_PAGE


class GenreService():
    def __init__(self, dao):
        self.dao = dao

    def get_one(self, g_id):
        return self.dao.get_one(g_id)

    def get_all(self, data):
        query=self.dao.get_all()

        if data.get("page") is not None:
            page = int(data.get("page"))
            return query.paginate(page, AMOUNT_POSTS_PER_PAGE, False).items
        else:
            count_items = query.all()
            return query.paginate(1, len(count_items), False).items
