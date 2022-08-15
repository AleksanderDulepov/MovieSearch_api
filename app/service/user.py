import base64
import hashlib
import hmac

from app.dao.models.user import User
from app.helper.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS


class UserService():
    def __init__(self, dao):
        self.dao = dao

    def get_one(self, u_id):
        return self.dao.get_one(u_id)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_id_by_email(self, email):
        user = self.get_by_email(email)
        user_id = user.id
        return user_id

    def do_post(self, data):
        data.pop('id', None)  # удалить id, если он будет передан
        # хеширование пароля перед записью в БД:
        data['password'] = self.make_user_password_hash(data.get('password'))
        new_item = User(**data)
        return self.dao.do_post(new_item)

    def do_put(self, email, data):
        item = self.get_by_email(email)
        old_input_password = data.get('password_1', None)
        new_input_password = data.get('password_2', None)
        old_password_from_db = item.password

        # проверка соответствия data['password_1'] паролю из базы, полученному по емейлу из токена:
        if None not in [old_input_password, new_input_password]:
            if self.compare_password(old_password_from_db, old_input_password):
                new_hash_password = self.make_user_password_hash(new_input_password)
                item.password = new_hash_password
                return self.dao.do_post(item)
            return None
        return None


    def do_patch(self, email, data):
        data.pop('id', None)  # удалить id, если он будет передан
        data.pop('email', None)  # удалить email, если он будет передан
        data.pop('password', None)  # удалить password, если он будет передан
        return self.dao.do_update(email, data)

    def make_user_password_hash(self, password):
        hash_digest = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), PWD_HASH_SALT, PWD_HASH_ITERATIONS)
        return base64.b64encode(hash_digest)


    def compare_password(self, hash_password_from_db, client_input_password):
        decoded_digest_db = base64.b64decode(hash_password_from_db)  # в байт-код
        hash_digest_client = self.make_user_password_hash(client_input_password)
        decoded_digest_client = base64.b64decode(hash_digest_client)

        return hmac.compare_digest(decoded_digest_db, decoded_digest_client)
