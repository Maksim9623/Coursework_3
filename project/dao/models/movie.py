from marshmallow import Schema, fields

from project.dao.models.base import BaseModel
from project.dao.models.director import Director
from project.dao.models.genre import Genre
from project.setup.db import db


class Movie(BaseModel):
    __tablename__ = 'movies'

    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.ForeignKey(Genre.id))
    #genre = db.relationship("Genres")
    director_id = db.Column(db.ForeignKey(Director.id))
    #director = db.relationship("Directors")


class MovieSchema(Schema):

    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Int()
