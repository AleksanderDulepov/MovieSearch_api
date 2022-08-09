from app.dao.models.bookmark import Bookmark


class BookmarkDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, b_id):
        item = self.session.query(Bookmark).get(b_id)
        return item

    def do_post(self, item):
        try:
            self.session.add(item)
            self.session.commit()
            self.session.close()
            return ""
        except:
            return None

    def find_item_to_del(self, m_id, user_id):
        item = self.session.query(Bookmark).filter(Bookmark.user_id == user_id, Bookmark.movie_id == m_id).first()
        return item

    def do_delete(self, b_id):
        try:
            item = self.get_one(b_id)
            self.session.delete(item)
            self.session.commit()
            self.session.close()
            return ""
        except:
            return None
