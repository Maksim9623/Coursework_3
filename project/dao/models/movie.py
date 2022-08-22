from marshmallow import Schema, fields


from project.dao.models.director import Director
from project.dao.models.genre import Genre
from project.setup.db import db
from project.setup.db.models import Base


class Movie(Base):
    __tablename__ = 'movies'

    title = db.Column(db.String(255))
    description = db.Column(db.String(255))
    trailer = db.Column(db.String(255))
    year = db.Column(db.Integer)
    rating = db.Column(db.Float)
    genre_id = db.Column(db.ForeignKey(Genre.id))
    genre = db.relationship("Genre")
    director_id = db.Column(db.ForeignKey(Director.id))
    director = db.relationship("Director")


class MovieSchema(Schema):
### Схема для сериализации ###

    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
