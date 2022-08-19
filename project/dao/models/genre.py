from marshmallow import Schema, fields

from project.dao.models.base import BaseModel
from project.setup.db import db


class Genre(BaseModel):
    __tablename__ = 'genres'

    name = db.Column(db.String(255), unique=True, nullable=False)


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()
