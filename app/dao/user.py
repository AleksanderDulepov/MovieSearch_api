from app.dao.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, u_id):
        item = self.session.query(User).get(u_id)
        return item

    def get_by_email(self, email):
        item = self.session.query(User).filter(User.email == email).first()
        return item

    def do_post(self, item):
        try:
            self.session.add(item)
            self.session.commit()
            self.session.close()
            return ""
        except:
            return None

    def do_update(self, email, data):
        try:
            self.session.query(User).filter(User.email == email).update(data)
            self.session.commit()
            self.session.close()
            return ""
        except:
            return None
