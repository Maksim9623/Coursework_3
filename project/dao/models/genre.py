from marshmallow import Schema, fields
from sqlalchemy import Column, String

from project.setup.db.models import Base


class Genre(Base):
    __tablename__ = 'genres'

    name = Column(String(255), unique=True, nullable=False)


class GenreSchema(Schema):
    ### Схема для сериализации ###
    id = fields.Int()
    name = fields.Str()
