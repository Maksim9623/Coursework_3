from marshmallow import Schema, fields

from project.dao.models.base import BaseModel
from project.models import Genre
from project.setup.db import db


class User(BaseModel):
    __tablename__ = 'users'

    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    favorite_genre = db.Column(db.ForeignKey(Genre.id))


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str(required=True)
    password_hash = fields.Str(required=True)
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()
