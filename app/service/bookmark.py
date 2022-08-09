from app.dao.models.bookmark import Bookmark


class BookmarkService():
    def __init__(self, bookmark_dao, user_service):
        self.bookmark_dao = bookmark_dao
        self.user_service = user_service

    def do_post(self, m_id, email):
        user_id = self.user_service.get_id_by_email(email)
        data = {"user_id": user_id, "movie_id": m_id}
        new_item = Bookmark(**data)
        return self.bookmark_dao.do_post(new_item)

    def delete_one(self, m_id, email):
        user_id = self.user_service.get_id_by_email(email)
        item_to_del = self.bookmark_dao.find_item_to_del(m_id, user_id)
        if item_to_del is not None:
            boormark_id = item_to_del.id
            return self.bookmark_dao.do_delete(boormark_id)
        return None
