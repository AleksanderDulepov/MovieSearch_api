from app.dao.models.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, g_id):
        item = self.session.query(Genre).get(g_id)
        return item

    def get_all(self):
        all_items = self.session.query(Genre)
        return all_items
