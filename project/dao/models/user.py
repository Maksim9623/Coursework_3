from marshmallow import Schema, fields
from sqlalchemy import Column, String, ForeignKey

from project.dao.models.genre import Genre
from project.setup.db.models import Base


class User(Base):
    __tablename__ = 'users'

    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    name = Column(String(255))
    surname = Column(String(255))
    favorite_genre = Column(ForeignKey(Genre.id))


### Схемы для сериализации ###


class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str(required=True)
    password_hash = fields.Str(required=True)
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Str()


class AuthUserSchema(Schema):
    id = fields.Int()
    email = fields.Str(required=True)
    password_hash = fields.Str(required=True)


class AuthRegisterRequest(Schema):
    email = fields.Str(required=True)
    password_hash = fields.Str(required=True)

