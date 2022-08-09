from app.dao.models.director import Director


class DirectorDAO:
    def __init__(self,session):
        self.session=session

    def get_one(self, d_id):
        item = self.session.query(Director).get(d_id)
        return item

    def get_all(self):
        all_items = self.session.query(Director)
        return all_items
