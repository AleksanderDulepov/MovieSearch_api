from sqlalchemy import desc

from app.dao.models.movie import Movie


class MovieDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, d_id):
        item = self.session.query(Movie).get(d_id)
        return item

    def get_all(self):
        all_items = self.session.query(Movie)
        return all_items

    def get_with_filter(self, is_sorted=False):
        all_items = self.get_all()
        if is_sorted:
            all_items = all_items.order_by(desc(Movie.year))
        return all_items
