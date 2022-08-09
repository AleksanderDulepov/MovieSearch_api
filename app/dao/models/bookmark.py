from marshmallow import Schema, fields

from app.database import db


class Bookmark(db.Model):
    __tablename__ = 'bookmark'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"))
    user = db.relationship("User")
    movie = db.relationship("Movie")


class BookmarkSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int()
    movie_id = fields.Int()
